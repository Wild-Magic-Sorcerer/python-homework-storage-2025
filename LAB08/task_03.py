#!/usr/bin/env python3
"""Разбиение строки на слова по знакам препинания."""

import re


def split_words(text: str) -> list[str]:
    """Разбивает по .,?!- и пробелам."""
    return [w for w in re.split(r"[.,?!\-\s]+", text) if w]


def main() -> None:
    text = input("Строка: ")
    words = split_words(text)
    print(f"Слова ({len(words)}): {words}")


if __name__ == "__main__":
    main()
