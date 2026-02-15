from datetime import datetime
date_time = input("Введите дату и время в формате ДД.ММ.ГГГГ ЧЧ:ММ:СС:")
try:
    dt = datetime.strptime(date_input, "%d.%m.%Y %H:%M:%S")
    print(f"День: {dt_day}")
    print(f"Месяц: {dt_month}")
    print(f"Год: {dt_year}")
    print(f"Часы: {dt_hour}")
    print(f"Минуты: {dt_minute}")
    print(f"Секунды: {dt_second}")
except ValueError:
    print("Ошибка:Введен не верный формат времени")
