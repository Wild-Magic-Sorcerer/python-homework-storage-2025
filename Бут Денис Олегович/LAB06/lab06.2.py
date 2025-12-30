class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    def deposit (self, amount):
        self.balance += amount
        return f"Остаток после после депозита: {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Остаток после снятия: {self.balance}"
        return f"Снятие превышает допустимый баланс ,текущий баланс: {self.balance}"

    def get_balance(self):
        return f"Текущий баланс: {self.balance}"


if __name__ == "__main__":
     some_money = int(input())
     some_deposit = int(input())
     some_withdraw = int(input())

     account = BankAccount(some_money)
     print(account.get_balance())
     print(account.deposit(some_deposit))
     print(account.withdraw(some_withdraw))

