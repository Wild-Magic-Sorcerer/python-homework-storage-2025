import re

if __name__== "__main__":
    text = input("Введите строку для поиска номера телефона: ")
    pattern = r'\+(\d)\((\d{3})\)((\d)-(\d{2}-\d{2}))'
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
    


