#!/usr/bin/env python3
"""Замена дат формата ДД.ММ.ГГГГ на DD.MM.YYYY."""

import re

DATE_PATTERN = r"\d{2}\.\d{2}\.\d{4}"


def replace_dates(text: str) -> tuple[str, int]:
    """Заменяет даты, возвращает (результат, кол-во)."""
    count = len(re.findall(DATE_PATTERN, text))
    result = re.sub(DATE_PATTERN, "DD.MM.YYYY", text)
    return result, count


def main() -> None:
    text = input("Строка: ")
    result, count = replace_dates(text)
    print(f"Замен: {count}")
    print(f"Результат: {result}")


if __name__ == "__main__":
    main()
