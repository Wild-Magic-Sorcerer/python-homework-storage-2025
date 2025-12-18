#!/usr/bin/env python3
"""BankAccount с инкапсуляцией баланса."""


class BankAccount:
    """Счёт с приватным балансом."""
    
    def __init__(self, balance: float = 0.0) -> None:
        self._balance = balance
    
    def deposit(self, amount: float) -> bool:
        """Пополнение."""
        if amount <= 0:
            print("Сумма должна быть > 0")
            return False
        self._balance += amount
        print(f"+{amount:.2f}, баланс: {self._balance:.2f}")
        return True
    
    def withdraw(self, amount: float) -> bool:
        """Снятие."""
        if amount <= 0:
            print("Сумма должна быть > 0")
            return False
        if amount > self._balance:
            print(f"Недостаточно средств ({self._balance:.2f})")
            return False
        self._balance -= amount
        print(f"-{amount:.2f}, баланс: {self._balance:.2f}")
        return True
    
    def get_balance(self) -> float:
        return self._balance


def main() -> None:
    acc = BankAccount(1000)
    print(f"Баланс: {acc.get_balance()}")
    
    acc.deposit(500)
    acc.withdraw(200)
    acc.withdraw(2000)


if __name__ == "__main__":
    main()
