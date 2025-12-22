#!/usr/bin/env python3
from typing import Any

VOWEL_SET = frozenset("аеёиоуыэюяaeiouАЕЁИОУЫЭЮЯAEIOU")
MIN_VOWEL_COUNT = 3

def count_vowels_in_string(text: str) -> int:
    return sum(1 for char in text if char in VOWEL_SET)


def filter_strings_with_vowels(**named_args: Any) -> dict[str, str]:
    filtered: dict[str, str] = {}
    
    for key, value in named_args.items():
        if isinstance(value, str) and count_vowels_in_string(value) >= MIN_VOWEL_COUNT:
            filtered[key] = value
    
    return filtered


def main() -> None:
    sample_data = {
        "name": "Александр",
        "city": "Москва",
        "country": "Россия",
        "age": 25,
        "greeting": "Привет",
        "farewell": "До свидания",
    }
    
    result = filter_strings_with_vowels(**sample_data)
    print(f"Аргументы со строками (>= {MIN_VOWEL_COUNT} гласных): {result}")


if __name__ == "__main__":
    main()
