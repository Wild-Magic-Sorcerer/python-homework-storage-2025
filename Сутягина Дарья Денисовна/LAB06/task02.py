class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # приватное поле

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Сумма пополнения должна быть положительной")

    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма снятия должна быть положительной")
        elif amount > self.__balance:
            print("Недостаточно средств на счёте")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account1 = BankAccount(1000)
account2 = BankAccount(500)

account1.deposit(300)
account1.withdraw(200)

account2.withdraw(700)   # попытка снять больше, чем есть
account2.deposit(150)

print("Баланс account_1:", account1.get_balance())
print("Баланс account_2:", account2.get_balance())

account = BankAccount(1000)

try:
    print(account.__balance)
except AttributeError:
    print("Ошибка доступа: приватный баланс.")
