#!/usr/bin/env python3
"""Разбиение строки на кортеж слов с подсчётом уникальных."""


def main() -> None:
    text = input("Слова через пробел: ")
    words = tuple(text.split())
    
    if not words:
        print("Пустой ввод")
        return
    
    print(f"Кортеж: {words}")
    print(f"Всего: {len(words)}, уникальных: {len(set(words))}")


if __name__ == "__main__":
    main()
