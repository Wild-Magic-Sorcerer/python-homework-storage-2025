if __name__ == "__main__":
    date = input("введите дату и время в формате ДД.ММ.ГГГГ ЧЧ:ММ:СС")

    date_part, time_part = date.split()
    day, month, year = map(int, date_part.split('.'))
    hour, minute, second = map(int, time_part.split(':'))

    print(f"День: {day:02d}",
            f"Месяц: {month:02d}",
            f"Год: {year:04d}",
            f"Часы: {hour:02d}",
            f"Минуты: {minute:02d}",
            f"Секунды: {second:02d}")

