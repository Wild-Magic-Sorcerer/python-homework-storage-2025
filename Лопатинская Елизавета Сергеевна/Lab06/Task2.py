class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance if initial_balance >= 0 else 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Пополнение на {amount}. Текущий баланс: {self.__balance}")
        else:
            print("Сумма пополнения должна быть положительной!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма снятия должна быть положительной!")
        elif amount > self.__balance:
            print(f"Ошибка: Недостаточно средств! (Запрошено: {amount}, Доступно: {self.__balance})")
        else:
            self.__balance -= amount
            print(f"Снято {amount}. Остаток на счете: {self.__balance}")

    def get_balance(self):
        return self.__balance

#Проверка работы


account_1 = BankAccount("Алексей", 1000)
account_2 = BankAccount("Мария", 500)


print(f"Счет владельца: {account_1.owner}")
account_1.deposit(500)
account_1.withdraw(2000)
account_1.withdraw(300)

print(f"Финальный баланс: {account_1.get_balance()}")

print("-" * 30)
try:
    print(account_1.__balance)
except AttributeError:

    print("Результат проверки: Прямой доступ к '__balance' невозможен. Поле защищено!")
    
