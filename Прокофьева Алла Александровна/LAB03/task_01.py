#!/usr/bin/env python3
"""Фильтрация строк длиннее средней длины."""


def filter_above_average(strings: list[str]) -> list[str]:
    """Возвращает строки с длиной больше средней."""
    if not strings:
        return []
    avg = sum(len(s) for s in strings) / len(strings)
    return [s for s in strings if len(s) > avg]


def main() -> None:
    data = ["кот", "собака", "слон", "крокодил", "мышь", "бегемот", "лев", "жираф"]
    avg = sum(len(s) for s in data) / len(data)
    
    print(f"Список: {data}")
    print(f"Средняя длина: {avg:.2f}")
    print(f"Длиннее средней: {filter_above_average(data)}")


if __name__ == "__main__":
    main()
