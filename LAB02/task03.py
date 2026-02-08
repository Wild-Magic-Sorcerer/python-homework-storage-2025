if __name__ == '__main__':
    text = input("Введите строку: ")

    vowels = "аеёиоуыэюяaeiouy"
    result = ""

    for char in text:
        if char.isalpha():
            if char.lower() in vowels:
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char

    print(f"Ваша строка: '{text}'")
    print(f"Результат: '{result}'")