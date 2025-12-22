#!/usr/bin/env python3
import re
from typing import TypedDict


class PhoneComponents(TypedDict):
    country: str
    city: str
    number: str
    full: str


PHONE_PATTERN = r"\+(\d)\((\d{3})\)(\d-\d{2}-\d{2})"


def extract_phone_number(input_text: str) -> PhoneComponents | None:
    match = re.search(PHONE_PATTERN, input_text)
    if not match:
        return None
    
    return {
        "country": match.group(1),
        "city": match.group(2),
        "number": match.group(3),
        "full": match.group(0),
    }


def display_phone_info(phone_data: PhoneComponents) -> None:
    print(f"Найден номер: {phone_data['full']}")
    print(f"  Код страны: +{phone_data['country']}")
    print(f"  Код города: {phone_data['city']}")
    print(f"  Номер абонента: {phone_data['number']}")


def main() -> None:
    user_input = input("Введите строку для поиска номера телефона: ")
    phone_info = extract_phone_number(user_input)
    
    if phone_info is None:
        print("Номер телефона не найден")
    else:
        display_phone_info(phone_info)


if __name__ == "__main__":
    main()
