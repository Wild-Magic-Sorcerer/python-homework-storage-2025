def parse_datetime_string(datetime_str):

    try:

        date_part, time_part = datetime_str.split(' ')
        day, month, year = date_part.split('.')
        hours, minutes, seconds = time_part.split(':')

        print("День:", day)
        print("Месяц:", month)
        print("Год:", year)
        print("Часы:", hours)
        print("Минуты:", minutes)
        print("Секунды:", seconds)

    except ValueError:
        print("Ошибка: Неверный формат введенной строки.")
        print("Пожалуйста, используйте формат ДД.ММ.ГГГГ ЧЧ:ММ:СС.")
    except IndexError:
        print("Ошибка: Неверный формат введенной строки. Не удалось разделить на части.")
        print("Пожалуйста, используйте формат ДД.ММ.ГГГГ ЧЧ:ММ:СС.")

user_input = input("Введите дату и время в формате ДД.ММ.ГГГГ ЧЧ:ММ:СС: ")

parse_datetime_string(user_input)
