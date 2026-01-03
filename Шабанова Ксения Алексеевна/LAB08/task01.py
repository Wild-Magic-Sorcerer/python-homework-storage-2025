import re

text = input("Введите строку: ")

# Группы в скобках позволят нам достать части номера отдельно
pattern = r"\+(\d)\((\d{3})\)(\d-\d{2}-\d{2})"

match = re.search(pattern, text)

if match:
    full_number = match.group(0)
    country_code = match.group(1)
    city_code = match.group(2)
    subscriber_number = match.group(3)
    
    print(f"Найден номер: {full_number}")
    print(f"Код страны: {country_code}")
    print(f"Код города: {city_code}")
    print(f"Номер абонента: {subscriber_number}")
else:
    print("Номер не найден")