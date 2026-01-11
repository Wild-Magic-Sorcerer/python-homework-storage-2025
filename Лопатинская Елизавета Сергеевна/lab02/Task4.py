from datetime import datetime
date_string = input("Введите дату и время в формате ДД.ММ.ГГГГ ЧЧ:ММ:СС: ")

try:
    dt_obj = datetime.strptime(date_string, "%d.%m.%Y %H:%M:%S")

    print(f"День: {dt_obj.day}")
    print(f"Месяц: {dt_obj.month}")
    print(f"Год: {dt_obj.year}")
    print(f"Часы: {dt_obj.hour}")
    print(f"Минуты: {dt_obj.minute}")
    print(f"Секунды: {dt_obj.second}")

except ValueError:
    print("Ошибка: Неверный формат даты. Пожалуйста, используйте шаблон ДД.ММ.ГГГГ ЧЧ:ММ:СС")

