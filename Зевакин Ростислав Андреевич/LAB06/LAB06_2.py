class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance


if __name__ == "__main__":
    account = BankAccount(20184)
    account.deposit(3500)
    account.withdraw(124)
    print(f"Баланс: {account.get_balance()}")

