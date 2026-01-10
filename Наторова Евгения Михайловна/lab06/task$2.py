class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
        print(f"зачисление: {amount}, ваш баланс: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print('на вашем счете недостаточно средств')
        else:
            self.__balance -= amount
            print(f"снято: {amount}, ваш баланс: {self.__balance}")
    def get_balance(self):
        return self.__balance

if __name__ == "__main__":
    account1 = BankAccount(10000)
    account1.deposit(5000)
    account1.withdraw(1000)
    account1.get_balance()

    account2 = BankAccount(10000)
    account2.deposit(4000)
    account2.withdraw(3000)
    account2.get_balance()

    print(f"баланс аккаунта1 get_balance(): {account1.get_balance()} ")

