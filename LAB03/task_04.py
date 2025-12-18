#!/usr/bin/env python3
"""Фильтрация kwargs: строки с >= 3 гласными."""

from typing import Any

VOWELS = frozenset("аеёиоуыэюяaeiouАЕЁИОУЫЭЮЯAEIOU")


def filter_by_vowels(**kwargs: Any) -> dict[str, str]:
    """Возвращает только строки с >= 3 гласными."""
    def vowel_count(s: str) -> int:
        return sum(c in VOWELS for c in s)
    
    return {k: v for k, v in kwargs.items()
            if isinstance(v, str) and vowel_count(v) >= 3}


def main() -> None:
    data = {
        "name": "Александр",      # 4 гласных
        "city": "Москва",         # 2 гласных
        "country": "Россия",      # 3 гласных
        "age": 25,                # не строка
        "greeting": "Привет",     # 2 гласных
        "farewell": "До свидания",  # 5 гласных
    }
    
    print(f"Фильтр (>= 3 гласных): {filter_by_vowels(**data)}")


if __name__ == "__main__":
    main()
