#!/usr/bin/env python3
"""Анализ строки: подсчёт слов, букв, цифр, пробелов, знаков препинания."""

import string


def analyze_string(text: str) -> dict[str, int]:
    """Возвращает статистику по строке."""
    text = text.strip()
    return {
        "words": len(text.split()) if text else 0,
        "letters": sum(c.isalpha() for c in text),
        "digits": sum(c.isdigit() for c in text),
        "spaces": sum(c.isspace() for c in text),
        "punctuation": sum(c in string.punctuation for c in text),
    }


def main() -> None:
    text = input("Строка: ")
    stats = analyze_string(text)
    
    print(f"\nСлов: {stats['words']}")
    print(f"Букв: {stats['letters']}")
    print(f"Цифр: {stats['digits']}")
    print(f"Пробелов: {stats['spaces']}")
    print(f"Знаков: {stats['punctuation']}")


if __name__ == "__main__":
    main()
