#!/usr/bin/env python3
from typing import TypedDict


class DateTimeComponents(TypedDict):
    day: str
    month: str
    year: str
    hours: str
    minutes: str
    seconds: str


EXPECTED_DATE_PARTS = 3
EXPECTED_TIME_PARTS = 3
EXPECTED_MAIN_PARTS = 2


def extract_datetime_components(input_string: str) -> DateTimeComponents | None:
    trimmed = input_string.strip()
    main_components = trimmed.split()
    
    if len(main_components) != EXPECTED_MAIN_PARTS:
        return None
    
    date_string = main_components[0]
    time_string = main_components[1]
    
    date_components = date_string.split(".")
    time_components = time_string.split(":")
    
    if (
        len(date_components) != EXPECTED_DATE_PARTS
        or len(time_components) != EXPECTED_TIME_PARTS
    ):
        return None
    
    return {
        "day": date_components[0],
        "month": date_components[1],
        "year": date_components[2],
        "hours": time_components[0],
        "minutes": time_components[1],
        "seconds": time_components[2],
    }


def display_components(components: DateTimeComponents) -> None:
    print(f"День: {components['day']}")
    print(f"Месяц: {components['month']}")
    print(f"Год: {components['year']}")
    print(f"Часы: {components['hours']}")
    print(f"Минуты: {components['minutes']}")
    print(f"Секунды: {components['seconds']}")


def main() -> None:
    print("Введите дату и время в формате: ДД.ММ.ГГГГ ЧЧ:ММ:СС")
    user_input = input("Ввод: ")
    
    components = extract_datetime_components(user_input)
    if components is None:
        print("Ошибка: неверный формат ввода")
        return
    
    print()
    display_components(components)


if __name__ == "__main__":
    main()
