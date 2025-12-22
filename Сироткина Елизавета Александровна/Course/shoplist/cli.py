import argparse
import logging
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

from shoplist import ShoppingList, __version__
from shoplist.exceptions import CategoryNotFoundError, ShoppingListError, ValidationError

logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

DEFAULT_PATH = Path.home() / ".shoplist" / "list.json"


def parse_decimal(value: str) -> Decimal:
    try:
        result = Decimal(value)
        if result < 0:
            raise ValidationError("Значение не может быть отрицательным")
        return result
    except InvalidOperation as e:
        raise ValidationError(f"Некорректное число: {value}") from e


def cmd_add_category(shop: ShoppingList, args: argparse.Namespace) -> int:
    try:
        category = shop.add_category(args.name)
        print(f"Добавлена категория: {category.name}")
        return 0
    except ValidationError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        return 1


def cmd_add_product(shop: ShoppingList, args: argparse.Namespace) -> int:
    try:
        product = shop.add_product(
            name=args.name,
            quantity=parse_decimal(args.quantity),
            price=parse_decimal(args.price),
            category_name=args.category,
        )
        print(f"Добавлен товар: {product}")
        return 0
    except (ValidationError, CategoryNotFoundError) as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        return 1


def cmd_list(shop: ShoppingList, args: argparse.Namespace) -> int:
    if args.category:
        products = shop.find_by_category(args.category)
        if not products:
            if shop.get_category(args.category):
                print(f'Категория "{args.category}" пуста')
            else:
                print(f'Категория "{args.category}" не найдена', file=sys.stderr)
                return 1
        else:
            print(f"\nКатегория: {args.category}")
            for p in products:
                print(f"  {p}")
    else:
        if not shop.categories:
            print("Список покупок пуст")
            return 0
        for cat in shop.categories:
            print(f"\n{cat.name} ({cat.count} товаров):")
            for p in cat.products:
                print(f"  {p}")
        print(f"\nОбщая стоимость: {shop.total_cost:.2f}")
    return 0


def cmd_find(shop: ShoppingList, args: argparse.Namespace) -> int:
    results = shop.find_product(args.name)
    if not results:
        print(f'Товар "{args.name}" не найден')
    else:
        for product, category in results:
            print(f"{product} (категория: {category.name})")
    return 0


def cmd_remove_product(shop: ShoppingList, args: argparse.Namespace) -> int:
    if shop.remove_product(args.name, args.category):
        print(f'Товар "{args.name}" удалён из категории "{args.category}"')
        return 0
    print(f'Товар "{args.name}" не найден в категории "{args.category}"', file=sys.stderr)
    return 1


def cmd_remove_category(shop: ShoppingList, args: argparse.Namespace) -> int:
    if not args.force:
        cat = shop.get_category(args.name)
        if cat and cat.count > 0:
            print(f'В категории "{args.name}" есть {cat.count} товаров')
            if input("Удалить категорию и все товары? (y/n): ").strip().lower() != "y":
                print("Отменено")
                return 0

    if shop.remove_category(args.name):
        print(f'Категория "{args.name}" удалена')
        return 0
    print(f'Категория "{args.name}" не найдена', file=sys.stderr)
    return 1


def cmd_categories(shop: ShoppingList, _: argparse.Namespace) -> int:
    if not shop.categories:
        print("Категорий нет")
        return 0
    print("Категории:")
    for cat in shop.categories:
        print(f"  {cat}")
    return 0


def cmd_sort(shop: ShoppingList, args: argparse.Namespace) -> int:
    try:
        shop.sort_products(args.category, args.by)
        print(f'Товары в категории "{args.category}" отсортированы по "{args.by}"')
        return 0
    except (CategoryNotFoundError, ValidationError) as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        return 1


def cmd_total(shop: ShoppingList, _: argparse.Namespace) -> int:
    print(f"Общая стоимость: {shop.total_cost:.2f}")
    return 0


def cmd_clear(shop: ShoppingList, args: argparse.Namespace) -> int:
    if shop.total_cost == 0:
        print("Список покупок пуст")
        return 0

    if not args.force:
        if input("Удалить все категории и товары? (y/n): ").strip().lower() != "y":
            print("Отменено")
            return 0

    deleted = shop.clear()
    print(f"Удалено категорий: {deleted}")
    return 0


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="shoplist",
        description="Управление списками покупок с категориями",
    )
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument("--data-file", type=Path, default=DEFAULT_PATH, help="Путь к файлу данных")

    sub = parser.add_subparsers(dest="cmd", metavar="КОМАНДА")

    p = sub.add_parser("add-category", help="Добавить категорию")
    p.add_argument("name", help="Название категории")

    p = sub.add_parser("add-product", help="Добавить товар")
    p.add_argument("name", help="Название товара")
    p.add_argument("quantity", help="Количество")
    p.add_argument("price", help="Цена за единицу")
    p.add_argument("category", help="Название категории")

    p = sub.add_parser("list", help="Список товаров")
    p.add_argument("-c", "--category", help="Фильтр по категории")

    p = sub.add_parser("find", help="Найти товар")
    p.add_argument("name", help="Название товара")

    p = sub.add_parser("remove-product", help="Удалить товар")
    p.add_argument("name", help="Название товара")
    p.add_argument("category", help="Название категории")

    p = sub.add_parser("remove-category", help="Удалить категорию")
    p.add_argument("name", help="Название категории")
    p.add_argument("-f", "--force", action="store_true", help="Без подтверждения")

    sub.add_parser("categories", help="Список категорий")

    p = sub.add_parser("sort", help="Сортировать товары")
    p.add_argument("category", help="Название категории")
    p.add_argument("--by", choices=["name", "price", "quantity", "cost"], default="name")

    sub.add_parser("total", help="Общая стоимость")

    p = sub.add_parser("clear", help="Очистить список")
    p.add_argument("-f", "--force", action="store_true", help="Без подтверждения")

    return parser


HANDLERS = {
    "add-category": cmd_add_category,
    "add-product": cmd_add_product,
    "list": cmd_list,
    "find": cmd_find,
    "remove-product": cmd_remove_product,
    "remove-category": cmd_remove_category,
    "categories": cmd_categories,
    "sort": cmd_sort,
    "total": cmd_total,
    "clear": cmd_clear,
}


def main() -> int:
    parser = create_parser()
    args = parser.parse_args()

    if not args.cmd:
        parser.print_help()
        return 0

    try:
        shop = ShoppingList(args.data_file)
    except ShoppingListError as e:
        print(f"Ошибка загрузки данных: {e}", file=sys.stderr)
        return 1

    try:
        return HANDLERS[args.cmd](shop, args)
    except ShoppingListError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
