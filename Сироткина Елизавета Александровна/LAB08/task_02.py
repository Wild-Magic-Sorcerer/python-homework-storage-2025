#!/usr/bin/env python3
import re

DATE_REGEX = r"\d{2}\.\d{2}\.\d{4}"
REPLACEMENT_TEMPLATE = "DD.MM.YYYY"


def replace_date_patterns(input_text: str) -> tuple[str, int]:
    matches = re.findall(DATE_REGEX, input_text)
    replacement_count = len(matches)
    modified_text = re.sub(DATE_REGEX, REPLACEMENT_TEMPLATE, input_text)
    
    return modified_text, replacement_count


def main() -> None:
    user_input = input("Введите строку с датами: ")
    result_text, replacement_count = replace_date_patterns(user_input)
    
    print(f"Количество замен: {replacement_count}")
    print(f"Результат: {result_text}")


if __name__ == "__main__":
    main()
