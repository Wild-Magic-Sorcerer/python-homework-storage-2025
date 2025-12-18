#!/usr/bin/env python3
"""Поиск телефона формата +x(xxx)x-xx-xx с помощью regex."""

import re


def find_phone(text: str) -> dict[str, str] | None:
    """Ищет телефон, возвращает dict с компонентами или None."""
    m = re.search(r"\+(\d)\((\d{3})\)(\d-\d{2}-\d{2})", text)
    if not m:
        return None
    return {"country": m.group(1), "city": m.group(2), "number": m.group(3), "full": m.group(0)}


def main() -> None:
    text = input("Строка: ")
    phone = find_phone(text)
    
    if not phone:
        print("Не найден")
    else:
        print(f"Найден: {phone['full']}")
        print(f"  Страна: +{phone['country']}, город: {phone['city']}")


if __name__ == "__main__":
    main()
