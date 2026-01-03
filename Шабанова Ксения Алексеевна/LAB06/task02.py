class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Приватное поле

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Пополнено: {amount}. Новый баланс: {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Снято: {amount}. Остаток: {self.__balance}")
        else:
            print("Ошибка: недостаточно средств или некорректная сумма!")

    def get_balance(self):
        return self.__balance

# Проверка
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(2000) # Проверка ограничения

print(f"Итоговый баланс: {account.get_balance()}")

# Проверка доступа извне
try:
    print(account.__balance)
except AttributeError:
    print("Доступ к приватной переменной __balance напрямую невозможен!")