class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Остаток после депозита: {self.__balance}"
        return f"Ошибка: сумма депозита должна быть положительной"

    def withdraw(self, amount):
        if amount <= 0:
            return f"Ошибка: сумма снятия должна быть положительной"

        if amount <= self.__balance:
            self.__balance -= amount
            return f"Остаток после снятия: {self.__balance}"
        return f"Снятие превышает допустимый баланс, текущий баланс: {self.__balance}"

    def get_balance(self):
        return f"Текущий баланс: {self.__balance}"


if __name__ == "__main__":
    some_money = int(input("Введите начальный баланс счета: "))
    some_deposit = int(input("Введите сумму для депозита: "))
    some_withdraw = int(input("Введите сумму для снятия: "))

    account = BankAccount(some_money)
    print(account.get_balance())
    print(account.deposit(some_deposit))
    print(account.withdraw(some_withdraw))