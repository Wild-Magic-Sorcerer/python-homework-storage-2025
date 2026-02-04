# Создайте класс BankAccount, который хранит приватное поле баланса.
# Реализуйте методы deposit(amount) и withdraw(amount)
# которые увеличивают и уменьшают баланс, не позволяя снимать сумму, превышающую остаток.
# Добавьте метод get_balance(), возвращающий текущий баланс.
# Проверьте работу на нескольких объектах, проверьте, возможен ли доступ к балансу извне.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return f"Пополнение на {amount}. Доступно: {self.__balance}"

    def withdraw(self, amount):
        if amount > self.__balance:
            return f"Недостаточно средств. Доступно: {self.__balance}"
        else:
            self.__balance -= amount
            return f"Снятие на {amount}. Доступно: {self.__balance}"

    def get_balance(self):
        return self.__balance

cash = BankAccount(100)
print(cash.deposit(100))
print(cash.withdraw(50))
