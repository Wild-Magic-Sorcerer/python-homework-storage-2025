import json
import logging
from decimal import Decimal
from pathlib import Path
from typing import Iterator

from shoplist.category import Category
from shoplist.exceptions import CategoryNotFoundError, StorageError, ValidationError
from shoplist.product import Product

logger = logging.getLogger(__name__)

ALLOWED_TEMP_DIRS = ("/tmp", "/var/folders", "/private/var/folders")


class ShoppingList:
    def __init__(self, storage_path: Path | str | None = None) -> None:
        self._categories: dict[str, Category] = {}
        self._path: Path | None = None

        if storage_path:
            self._path = self._validate_path(Path(storage_path))
            if self._path.exists():
                self._load()

    def _validate_path(self, path: Path) -> Path:
        try:
            resolved = path.resolve()
            home = Path.home()
            is_safe = (
                str(resolved).startswith(str(home))
                or any(str(resolved).startswith(d) for d in ALLOWED_TEMP_DIRS)
                or not resolved.is_absolute()
            )
            if resolved.is_absolute() and not is_safe:
                raise ValidationError(f"Небезопасный путь: {resolved}")
            return resolved
        except OSError as e:
            raise StorageError(f"Некорректный путь: {e}") from e

    def add_category(self, name: str) -> Category:
        key = name.lower()
        if key in self._categories:
            raise ValidationError(f'Категория "{name}" уже существует')
        category = Category(name=name)
        self._categories[key] = category
        self._save()
        logger.info("Добавлена категория: %s", name)
        return category

    def get_category(self, name: str) -> Category | None:
        return self._categories.get(name.lower())

    def remove_category(self, name: str) -> bool:
        key = name.lower()
        if key not in self._categories:
            return False
        del self._categories[key]
        self._save()
        logger.info("Удалена категория: %s", name)
        return True

    def add_product(
        self,
        name: str,
        quantity: Decimal | float | int,
        price: Decimal | float | int,
        category_name: str,
    ) -> Product:
        category = self.get_category(category_name)
        if category is None:
            available = ", ".join(self._categories.keys()) or "нет"
            raise CategoryNotFoundError(f'Категория "{category_name}" не найдена. Доступные: {available}')

        product = Product(
            name=name,
            quantity=Decimal(str(quantity)),
            price=Decimal(str(price)),
        )
        category.add_product(product)
        self._save()
        logger.info("Добавлен товар: %s в %s", name, category_name)
        return product

    def remove_product(self, name: str, category_name: str) -> bool:
        category = self.get_category(category_name)
        if not category:
            return False
        if category.remove_product(name):
            self._save()
            logger.info("Удалён товар: %s из %s", name, category_name)
            return True
        return False

    def find_product(self, name: str) -> list[tuple[Product, Category]]:
        results = []
        for category in self._categories.values():
            product = category.find_product(name)
            if product:
                results.append((product, category))
        return results

    def find_by_category(self, name: str) -> list[Product]:
        category = self.get_category(name)
        return list(category.products) if category else []

    @property
    def total_cost(self) -> float:
        return sum(c.total_cost for c in self._categories.values())

    @property
    def categories(self) -> list[Category]:
        return sorted(self._categories.values(), key=lambda c: c.name.lower())

    @property
    def all_products(self) -> list[Product]:
        return [p for c in self._categories.values() for p in c.products]

    def sort_products(self, category_name: str, by: str = "name") -> None:
        category = self.get_category(category_name)
        if not category:
            raise CategoryNotFoundError(f'Категория "{category_name}" не найдена')

        sort_keys = {
            "name": lambda p: p.name.lower(),
            "price": lambda p: p.price,
            "quantity": lambda p: p.quantity,
            "cost": lambda p: -p.total_cost,
        }
        if by not in sort_keys:
            raise ValidationError(f"Неизвестный критерий сортировки: {by}")

        category.products.sort(key=sort_keys[by])
        self._save()

    def clear(self) -> int:
        count = len(self._categories)
        self._categories.clear()
        self._save()
        logger.info("Очищено категорий: %d", count)
        return count

    def __iter__(self) -> Iterator[Category]:
        return iter(self.categories)

    def __len__(self) -> int:
        return len(self._categories)

    def _save(self) -> None:
        if not self._path:
            return
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            data = {
                "categories": [
                    {"name": c.name, "products": [p.to_dict() for p in c.products]}
                    for c in self._categories.values()
                ]
            }
            tmp = self._path.with_suffix(self._path.suffix + ".tmp")
            tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            tmp.replace(self._path)
        except (OSError, IOError) as e:
            logger.exception("Ошибка сохранения")
            raise StorageError(f"Ошибка сохранения: {e}") from e

    def _load(self) -> None:
        if not self._path or not self._path.exists():
            return
        try:
            content = self._path.read_text(encoding="utf-8")
            data = json.loads(content)
            if not isinstance(data, dict):
                raise ValidationError("Некорректный формат данных")

            self._categories.clear()
            for cat_data in data.get("categories", []):
                category = Category(name=cat_data["name"])
                for prod_data in cat_data.get("products", []):
                    category.add_product(Product.from_dict(prod_data))
                self._categories[category.name.lower()] = category
            logger.info("Загружено категорий: %d", len(self._categories))
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            logger.exception("Ошибка загрузки")
            raise StorageError(f"Ошибка загрузки: {e}") from e
