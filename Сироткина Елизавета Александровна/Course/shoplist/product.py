from dataclasses import dataclass
from decimal import Decimal

from shoplist.exceptions import ValidationError


@dataclass(frozen=True)
class Product:
    name: str
    quantity: Decimal
    price: Decimal

    def __post_init__(self) -> None:
        if not self.name or not self.name.strip():
            raise ValidationError("Название товара не может быть пустым")
        if self.quantity <= 0:
            raise ValidationError("Количество должно быть положительным")
        if self.price < 0:
            raise ValidationError("Цена не может быть отрицательной")

    @property
    def total_cost(self) -> Decimal:
        return self.quantity * self.price

    def __str__(self) -> str:
        return f"{self.name} — {self.quantity} × {self.price:.2f} = {self.total_cost:.2f}"

    def to_dict(self) -> dict[str, str]:
        return {
            "name": self.name,
            "quantity": str(self.quantity),
            "price": str(self.price),
        }

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> "Product":
        try:
            return cls(
                name=data["name"],
                quantity=Decimal(data["quantity"]),
                price=Decimal(data["price"]),
            )
        except (KeyError, ValueError) as e:
            raise ValidationError(f"Некорректные данные товара: {e}") from e
