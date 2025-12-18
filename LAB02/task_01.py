#!/usr/bin/env python3
"""Проверка строки на палиндром с указанием позиции несовпадения."""


def check_palindrome(text: str) -> tuple[bool, int | None]:
    """Возвращает (True, None) или (False, индекс несовпадения)."""
    n = len(text)
    for i in range(n // 2):
        if text[i] != text[n - 1 - i]:
            return False, i
    return True, None


def main() -> None:
    text = input("Введите строку: ")
    if not text:
        print("Пустая строка — палиндром")
        return
    
    ok, idx = check_palindrome(text)
    if ok:
        print(f"'{text}' — палиндром")
    else:
        r = len(text) - 1 - idx
        print(f"'{text}' — не палиндром")
        print(f"Несовпадение: индекс {idx} ('{text[idx]}') и индекс {r} ('{text[r]}')")


if __name__ == "__main__":
    main()
