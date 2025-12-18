#!/usr/bin/env python3
"""Использование map + lambda для получения длин строк."""


def main() -> None:
    words = ["apple", "banana", "cherry"]
    lengths = list(map(lambda s: len(s), words))
    
    print(f"Слова: {words}")
    print(f"Длины: {lengths}")


if __name__ == "__main__":
    main()
