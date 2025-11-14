def transform_vowels_consonants(input_string: str) -> str:

    vowels = "AEIOUaeiouАЕЁИОУЫЭЮЯаеёиоуыэюя"

    transformed_chars = []

    for char in input_string:
        if char.isalpha():
            if char in vowels:
                transformed_chars.append(char.upper())
            else:
                transformed_chars.append(char.lower())
        else:
            transformed_chars.append(char)

    return "".join(transformed_chars)

if __name__ == "__main__":
    test_strings = []

    for s in test_strings:
        transformed_s = transform_vowels_consonants(s)
        print(f"Оригинал: '{s}'")
        print(f"Результат: '{transformed_s}'")

    user_input = input("\nВведите свою строку для преобразования: ")
    user_transformed = transform_vowels_consonants(user_input)
    print(f"Ваша строка: '{user_input}'")
    print(f"Преобразованная: '{user_transformed}'")
