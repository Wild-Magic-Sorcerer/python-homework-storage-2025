#!/usr/bin/env python3
VOWEL_CHARS = frozenset("аеёиоуыэюяaeiouАЕЁИОУЫЭЮЯAEIOU")
CONSONANT_CHARS = frozenset(
    "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz"
    "БВГДЖЗЙКЛМНПРСТФХЦЧШЩBCDFGHJKLMNPQRSTVWXYZ"
)


def is_vowel(character: str) -> bool:
    return character in VOWEL_CHARS


def is_consonant(character: str) -> bool:
    return character in CONSONANT_CHARS


def transform_case(input_string: str) -> str:
    transformed_chars: list[str] = []
    
    for char in input_string:
        if is_vowel(char):
            transformed_chars.append(char.upper())
        elif is_consonant(char):
            transformed_chars.append(char.lower())
        else:
            transformed_chars.append(char)
    
    return "".join(transformed_chars)


def main() -> None:
    user_input = input("Введите строку для преобразования: ")
    result = transform_case(user_input)
    print(f"Результат: {result}")


if __name__ == "__main__":
    main()
