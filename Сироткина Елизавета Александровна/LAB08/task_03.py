#!/usr/bin/env python3
import re

SPLIT_PATTERN = r"[.,?!\-\s]+"


def tokenize_text(input_text: str) -> list[str]:
    tokens = re.split(SPLIT_PATTERN, input_text)
    return [token for token in tokens if token]


def main() -> None:
    user_input = input("Введите строку для разбиения на слова: ")
    word_list = tokenize_text(user_input)
    
    print(f"Найдено слов: {len(word_list)}")
    print(f"Список слов: {word_list}")


if __name__ == "__main__":
    main()
