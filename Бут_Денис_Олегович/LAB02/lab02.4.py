def parse_datetime(datetime_str):
    if not datetime_str:
        return None
    try:
        date_part, time_part = datetime_str.split()
        day, month, year = date_part.split('.')
        hours, minutes, seconds = time_part.split(':')

        return {'day': day,
            'month': month,
            'year': year,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds}

    except ValueError:
        print("Используйте: ДД.ММ.ГГГГ ЧЧ:ММ:СС")
    return None

if __name__ == "__main__":

    datetime_input = input("Введите дату и время:(ДД.ММ.ГГГГ ЧЧ:ММ:СС): ")
    result = parse_datetime(datetime_input)

    if result:
        print("\nРезультат:")
        print(f"День: {result['day']}")
        print(f"Месяц: {result['month']}")
        print(f"Год: {result['year']}")
        print(f"Часы: {result['hours']}")
        print(f"Минуты: {result['minutes']}")
        print(f"Секунды: {result['seconds']}")

