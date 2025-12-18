#!/usr/bin/env python3
"""Парсинг даты-времени формата ДД.ММ.ГГГГ ЧЧ:ММ:СС."""


def parse_datetime(s: str) -> dict[str, str] | None:
    """Парсит строку, возвращает компоненты или None."""
    parts = s.strip().split()
    if len(parts) != 2:
        return None
    
    date_parts = parts[0].split(".")
    time_parts = parts[1].split(":")
    
    if len(date_parts) != 3 or len(time_parts) != 3:
        return None
    
    return {
        "day": date_parts[0], "month": date_parts[1], "year": date_parts[2],
        "hours": time_parts[0], "minutes": time_parts[1], "seconds": time_parts[2],
    }


def main() -> None:
    print("Формат: ДД.ММ.ГГГГ ЧЧ:ММ:СС")
    s = input("Ввод: ")
    
    parsed = parse_datetime(s)
    if not parsed:
        print("Неверный формат")
        return
    
    print(f"\nДень: {parsed['day']}")
    print(f"Месяц: {parsed['month']}")
    print(f"Год: {parsed['year']}")
    print(f"Часы: {parsed['hours']}")
    print(f"Минуты: {parsed['minutes']}")
    print(f"Секунды: {parsed['seconds']}")


if __name__ == "__main__":
    main()
