import re


def format_phone_number(phone_number):
    if len(phone_number) == 9 and phone_number.isdigit():
        formatted_number = f"+{phone_number[0]}({phone_number[1:4]}){phone_number[4]}-{phone_number[5:7]}-{phone_number[7:9]}"
        return formatted_number
    else:
        return None


def find_phone_number(input_string):

    pattern = r'\+(\d)\((\d{3})\)(\d{1})-(\d{2})-(\d{2})'

    match = re.search(pattern, input_string)

    if match:
        country_code = match.group(1)
        city_code = match.group(2)
        subscriber_number = f"{match.group(3)}-{match.group(4)}-{match.group(5)}"

        print(
            f"Номер найден: Код страны: +{country_code}, Код города: {city_code}, Номер абонента: {subscriber_number}")
    else:
        print("Номер не найден")

user_input = input("Введите строку: ")

find_phone_number(user_input)

for word in user_input.split():
    formatted_number = format_phone_number(word)
    if formatted_number:
        print(f"Найден 9-значный номер: {formatted_number}")
        find_phone_number(formatted_number)
        break
else:
    print("Номер не найден")

    #сделал так, чтобы при обычном вводе переделывало под формат и все находило