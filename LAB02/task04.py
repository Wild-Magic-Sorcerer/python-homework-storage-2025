if __name__ == '__main__':
    while True:
        text = input("Введите дату и время (ДД.ММ.ГГГГ ЧЧ:ММ:СС): ")

        try:
            date, time = text.split()
            day, month, year = date.split(".")
            hour, minute, second = time.split(":")

            print("День:", day)
            print("Месяц:", month)
            print("Год:", year)
            print("Часы:", hour)
            print("Минуты:", minute)
            print("Секунды:", second)

            break

        except ValueError:
            print("Неверный формат\nИспользуйте формат ДД.ММ.ГГГГ ЧЧ:ММ:СС\n")

