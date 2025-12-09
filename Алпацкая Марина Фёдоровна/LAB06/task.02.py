class BankAccount:
    def __init__(self,balans):
        self.__balans = balans

    def deposit(self,amount):
        self.__balans += amount
        return self.__balans

    def withdraw(self,amount):
        if amount < self.__balans:
            self.__balans -= amount
        else: print('У вас на счёте недостаточно средств')
        return self.__balans

    def get_balance(self):
        return self.__balans

if __name__ == '__main__':
    balans_max = int(input(f'Введите баланс Макса: '))
    max_account = BankAccount(balans_max)

    deposit_max = input(f'Введите сколько Макс положил денег на баланс: ')
    max_account.deposit(int(deposit_max))

    withdraw_max = input(f'Введите сколько снял Макс с баланса: ')
    max_account.withdraw(int(withdraw_max))

    print(f'Текуший баланс Макса: {max_account.get_balance()}')
