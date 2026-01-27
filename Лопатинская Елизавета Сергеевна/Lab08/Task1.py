import re

def find_phone(text):
    pattern = r"\+(\d)\((\d{3})\)(\d-\d{2}-\d{2})"

    match = re.search(pattern, text)

    if match:
        country_code = match.group(1)
        city_code = match.group(2)
        subscriber_number = match.group(3)

        print("\n[Результат]: Номер найден!")
        print(f"Код страны:      {country_code}")
        print(f"Код города:      {city_code}")
        print(f"Номер абонента:  {subscriber_number}")
    else:
        print("\n[Результат]: Номер не найден")


def main():
    print("--- Программа поиска телефонных номеров ---")
    print("Ожидаемый формат: +7(999)1-22-33")
    user_input = input("\nВведите строку для поиска номера: ")
    
    find_phone(user_input)

if __name__ == "__main__":
    main()
    
