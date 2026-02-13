date_time = input("Введите дату и время в формате ДД.ММ.ГГГГ ЧЧ:ММ:СС: ")

parts = date_time.split(' ')

date_part = parts[0]
time_part = parts[1]

date_parts = date_part.split('.')
day = date_parts[0]
month = date_parts[1]
year = date_parts[2]

time_parts = time_part.split(':')
hours = time_parts[0]
minutes = time_parts[1]
seconds = time_parts[2]

print("День:", day)
print("Месяц:", month)
print("Год:", year)
print("Часы:", hours)
print("Минуты:", minutes)
print("Секунды:", seconds)