import re

def phone_number():
    text = input("Введите строку для поиска номера телефона: ")
    pattern = r'\+(\d)(\d{3})(\d{7})'
    match = re.search(pattern, text)

    if match:
        country_code = match.group(1)
        city_code = match.group(2)
        subscriber_number = match.group(3)
        print(f"Найден номер телефона:")
        print(f"Код страны: {country_code}")
        print(f"Код города: {city_code}")
        print(f"Номер абонента: {subscriber_number}")
    else:
        print("Номер не найден")


phone_number()