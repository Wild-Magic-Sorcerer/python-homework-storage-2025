import re

if __name__ == "__main__":
    text = input("Cтрока для поиска телефона: ")
    pattern = r"\+(\d)\((\d{3})\)(\d-\d{2}-\d{2})"
    match = re.search(pattern, text)

    if match:
        country_code = match.group(1)
        city_code = match.group(2)
        subscriber_number = match.group(3)
        print(f"Номер телефона: код страны: {country_code}, "
              f"код города: {city_code}, полный номер: +{country_code}({city_code}){subscriber_number} "
              f"номер абонента: {subscriber_number},")
    else:

        print("Номер не найден")


