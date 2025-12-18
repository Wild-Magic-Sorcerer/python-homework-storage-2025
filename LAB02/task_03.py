#!/usr/bin/env python3
"""Преобразование: гласные в верхний регистр, согласные в нижний."""

VOWELS = frozenset("аеёиоуыэюяaeiouАЕЁИОУЫЭЮЯAEIOU")
CONSONANTS = frozenset("бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz"
                       "БВГДЖЗЙКЛМНПРСТФХЦЧШЩBCDFGHJKLMNPQRSTVWXYZ")


def transform(text: str) -> str:
    """Гласные -> upper, согласные -> lower."""
    result = []
    for ch in text:
        if ch in VOWELS:
            result.append(ch.upper())
        elif ch in CONSONANTS:
            result.append(ch.lower())
        else:
            result.append(ch)
    return "".join(result)


def main() -> None:
    text = input("Строка: ")
    print(f"Результат: {transform(text)}")


if __name__ == "__main__":
    main()
