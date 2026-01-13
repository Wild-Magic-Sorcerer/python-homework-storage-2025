def parse_datetime(datetime_str):
    date_str, time_str = datetime_str.split()
    day, month, year = date_str.split('.')
    hours, minutes, seconds = time_str.split(':')
    print("День:", day)
    print("Месяц:", month)
    print("Год:", year)
    print("Часы:", hours)
    print("Минуты:", minutes)
    print("Секунды:", seconds)

user_input = input("Введите дату и время в формате 'ДД.ММ.ГГГГ ЧЧ:ММ:СС': ")
parse_datetime(user_input)