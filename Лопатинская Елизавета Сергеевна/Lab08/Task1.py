import re

def find_phone(text):
    pattern = r"\+(\d)\((\d{3})\)(\d-\d{2}-\d{2})"

    match = re.search(pattern, text)

    if match:
        country_code = match.group(1)
        city_code = match.group(2)
        subscriber_number = match.group(3)

        print("Номер найден!")
        print(f"Код страны: {country_code}")
        print(f"Код города: {city_code}")
        print(f"Номер абонента: {subscriber_number}")
    else:
        print("Номер не найден")


user_input = input("Введите строку для поиска номера: ")

find_phone(user_input)

