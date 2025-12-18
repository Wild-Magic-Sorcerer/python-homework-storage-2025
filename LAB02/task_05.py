#!/usr/bin/env python3
"""Сравнение слов двух строк без учёта регистра и пунктуации."""

import string


def extract_words(text: str) -> set[str]:
    """Извлекает слова в lowercase, убирая пунктуацию."""
    cleaned = text.translate(str.maketrans("", "", string.punctuation))
    return set(cleaned.lower().split())


def main() -> None:
    words1 = extract_words(input("Первая строка: "))
    words2 = extract_words(input("Вторая строка: "))
    
    only1 = words1 - words2
    only2 = words2 - words1
    
    if not only1 and not only2:
        print("\nСлова идентичны")
    else:
        if only1:
            print(f"\nТолько в первой: {', '.join(sorted(only1))}")
        if only2:
            print(f"Только во второй: {', '.join(sorted(only2))}")


if __name__ == "__main__":
    main()
