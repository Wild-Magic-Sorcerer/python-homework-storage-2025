class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Внесено: {amount}. Текущий баланс: {self.__balance}")
        else:
            print("Сумма для внесения должна быть положительной.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Снято: {amount}. Текущий баланс: {self.__balance}")
        elif amount > self.__balance:
            print("Недостаточно средств для снятия.")
        else:
            print("Сумма для снятия должна быть положительной.")

    def get_balance(self):
        return self.__balance


def main():
    account = BankAccount()

    while True:
        print("\nВыберите операцию:")
        print("1. Внести деньги")
        print("2. Снять деньги")
        print("3. Проверить баланс")
        print("4. Выйти")

        choice = input("Введите номер операции (1-4): ")

        if choice == '1':
            amount = float(input("Введите сумму для внесения: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Введите сумму для снятия: "))
            account.withdraw(amount)
        elif choice == '3':
            print(f"Текущий баланс: {account.get_balance()}")
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите номер операции от 1 до 4.")


if __name__ == "__main__":
    main()