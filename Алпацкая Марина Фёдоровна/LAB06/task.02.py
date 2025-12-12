class BankAccount:
    def __init__(self,balans):
        self.__balans = balans

    def deposit(self,amount):
        self.__balans += amount

    def withdraw(self,amount):
        if amount <= self.__balans:
            self.__balans -= amount
        else: print('У вас на счёте недостаточно средств')

    def get_balance(self):
        return self.__balans

if __name__ == '__main__':
    while True:
        balans_max_str = input(f'Введите баланс Макса: ')
        try:
            balans_max = int(balans_max_str)
            break
        except ValueError:
            print("Ошибка, пожалуйста введите целочисленные значение")
    max_account = BankAccount(balans_max)

    while True:
        deposit_max_str = input(f'Введите сколько Макс положил денег на баланс: ')
        try:
            deposit_max = int(deposit_max_str)
            break
        except ValueError:
            print("Ошибка, пожалуйста введите целочисленные значение")
    max_account.deposit(int(deposit_max))

    while True:
        withdraw_max_str = input(f'Введите сколько снял Макс с баланса: ')
        try:
            withdraw_max = int(withdraw_max_str)
            break
        except ValueError:
            print("Ошибка, пожалуйста введите целочисленные значение")
    max_account.withdraw(int(withdraw_max))

    print(f'Текуший баланс Макса: {max_account.get_balance()}')
