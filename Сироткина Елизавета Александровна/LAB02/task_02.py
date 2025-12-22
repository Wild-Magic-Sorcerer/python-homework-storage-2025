#!/usr/bin/env python3
import string
from typing import TypedDict


class StringStats(TypedDict):
    words: int
    letters: int
    digits: int
    spaces: int
    punctuation: int


def count_words(cleaned_text: str) -> int:
    if not cleaned_text:
        return 0
    return len(cleaned_text.split())


def count_letters(text: str) -> int:
    return sum(1 for char in text if char.isalpha())


def count_digits(text: str) -> int:
    return sum(1 for char in text if char.isdigit())


def count_spaces(text: str) -> int:
    return sum(1 for char in text if char.isspace())


def count_punctuation(text: str) -> int:
    return sum(1 for char in text if char in string.punctuation)


def analyze_string(input_text: str) -> StringStats:
    normalized_text = input_text.strip()
    return {
        "words": count_words(normalized_text),
        "letters": count_letters(input_text),
        "digits": count_digits(input_text),
        "spaces": count_spaces(input_text),
        "punctuation": count_punctuation(input_text),
    }


def display_statistics(stats: StringStats) -> None:
    print(f"\nКоличество слов: {stats['words']}")
    print(f"Количество букв: {stats['letters']}")
    print(f"Количество цифр: {stats['digits']}")
    print(f"Количество пробелов: {stats['spaces']}")
    print(f"Количество знаков препинания: {stats['punctuation']}")


def main() -> None:
    user_input = input("Введите строку для анализа: ")
    statistics = analyze_string(user_input)
    display_statistics(statistics)


if __name__ == "__main__":
    main()
