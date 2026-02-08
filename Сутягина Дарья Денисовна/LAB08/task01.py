import re

text = input("Введите строку: ")

pattern = r"\+(\d)\((\d{3})\)(\d)-(\d{2})-(\d{2})"

match = re.search(pattern, text)

if match:
    country_code = match.group(1)
    city_code = match.group(2)
    subscriber_number = f"{match.group(3)}-{match.group(4)}-{match.group(5)}"

    print("Номер найден!")
    print("Код страны:", country_code)
    print("Код города:", city_code)
    print("Номер абонента:", subscriber_number)
else:
    print("Номер не найден")
