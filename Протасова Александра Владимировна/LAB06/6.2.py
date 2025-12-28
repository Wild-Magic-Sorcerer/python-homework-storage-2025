class BankAccount:
    def __init__(self, start_money=None):
        if not start_money:
           self.__money = 0
        else:
           self.__money = start_money

    def add_money(self, amount):
        """Положить деньги на счет"""
        if amount > 0:
            self.__money += amount

    def take_money(self, amount):
        """Снять деньги со счета"""
        if 0 < amount <= self.__money:
            self.__money -= amount
        else:
           raise ValueError("Невозможно снять указанную сумму")

    def show_money(self):
        """Показать баланс"""
        return self.__money

if __name__ == "__main__":
    my_account = BankAccount(1100)
    sasha_account = BankAccount(800)

    print(f"На счету: {my_account.show_money()} руб")

    try:
        my_account.take_money(20000)
        print('Успех, деньги сняты')
    except ValueError:
        print('Провал, мало денег')


    print(f"У Саши: {sasha_account.show_money()} руб")
    sasha_account.add_money(1000)
    print(f"Саша положила 1000 руб: {sasha_account.show_money()} руб")

    try:
        print(f"Попытка посмотреть my_account.__money")
        money = my_account.__money
        print(f"Удалось: {money}")
    except AttributeError:
        print("Ошибка:'__money' не найден")
        print("Python скрыл приватное поле!")
