#!/usr/bin/env python3

class BankAccount:
    def __init__(self, initial_balance: float = 0.0) -> None:
        self._balance = initial_balance
    
    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            print("Ошибка: сумма пополнения должна быть положительной")
            return False
        
        self._balance += amount
        print(f"Пополнение: +{amount:.2f}, текущий баланс: {self._balance:.2f}")
        return True
    
    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Ошибка: сумма снятия должна быть положительной")
            return False
        
        if amount > self._balance:
            print(
                f"Ошибка: недостаточно средств. "
                f"Текущий баланс: {self._balance:.2f}, запрошено: {amount:.2f}"
            )
            return False
        
        self._balance -= amount
        print(f"Снятие: -{amount:.2f}, текущий баланс: {self._balance:.2f}")
        return True
    
    def get_balance(self) -> float:
        return self._balance


def main() -> None:
    account = BankAccount(initial_balance=1000.0)
    print(f"Начальный баланс: {account.get_balance():.2f}")
    
    account.deposit(500.0)
    account.withdraw(200.0)
    account.withdraw(2000.0)


if __name__ == "__main__":
    main()
