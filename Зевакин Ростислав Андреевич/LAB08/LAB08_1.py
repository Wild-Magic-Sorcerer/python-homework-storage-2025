import re


def format_phone_number(phone):

    match = re.match(r'\+(\d)\((\d{3})\)(\d-\d{2}-\d{2})', phone)
    if match:
        country_code, city_code, subscriber_number = match.groups()
        return (f"Найден номер: {phone}\n"
                f"Код страны: {country_code}\n"
                f"Код города: {city_code}\n"
                f"Номер абонента: {subscriber_number}")
    return "Номер не найден"


def main():
    print("Введите строку для поиска номера телефона:")
    user_input = input()

    pattern = r'\+\d\(\d{3}\)\d-\d{2}-\d{2}'

    match = re.search(pattern, user_input)

    if match:
        phone_number = match.group()
        print(format_phone_number(phone_number))
    else:
        print("Номер не найден")


if __name__ == "__main__":
    main()