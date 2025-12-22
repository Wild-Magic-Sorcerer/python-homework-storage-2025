from dataclasses import dataclass, field
from typing import Iterator

from shoplist.exceptions import ValidationError
from shoplist.product import Product


@dataclass
class Category:
    name: str
    products: list[Product] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.name or not self.name.strip():
            raise ValidationError("Название категории не может быть пустым")

    def add_product(self, product: Product) -> None:
        if product is None:
            raise ValidationError("Товар не может быть None")
        self.products.append(product)

    def remove_product(self, name: str) -> bool:
        initial = len(self.products)
        self.products = [p for p in self.products if p.name.lower() != name.lower()]
        return len(self.products) < initial

    def find_product(self, name: str) -> Product | None:
        name_lower = name.lower()
        return next((p for p in self.products if p.name.lower() == name_lower), None)

    @property
    def total_cost(self) -> float:
        return float(sum(p.total_cost for p in self.products))

    @property
    def count(self) -> int:
        return len(self.products)

    def __iter__(self) -> Iterator[Product]:
        return iter(self.products)

    def __len__(self) -> int:
        return len(self.products)

    def __str__(self) -> str:
        return f"{self.name} ({self.count} товаров, {self.total_cost:.2f})"
