class BankAccount:
    def __init__(self, start_money=0):
        self.__money = start_money
    def add_money(self, amount):
        """Положить деньги на счет"""
        if amount > 0:
            self.__money += amount
            return True
        return False
    def take_money(self, amount):
        """Снять деньги со счета"""
        if 0 < amount <= self.__money:
            self.__money -= amount
            return True
        return False
    def show_money(self):
        """Показать баланс"""
        return self.__money

if __name__ == "__main__":
    my_account = BankAccount(1100)
    sasha_account = BankAccount(800)
    print(f"На счету: {my_account.show_money()} руб")

    if my_account.take_money(300):
        print("Успешно сняли 300 руб")
    else:
        print("Не удалось снять 300 руб")
    print(f"Осталось: {my_account.show_money()} руб")

    if my_account.take_money(2000):
        print("Сняли 2000 руб")
    else:
        print("Нельзя снять 2000 руб - мало денег")

    if my_account.add_money(500):
        print("Положили 500 руб")
    print(f"Итого: {my_account.show_money()} руб")

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
