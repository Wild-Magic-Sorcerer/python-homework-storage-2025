if __name__ == "__main__":
    text = input("введите строку: ")

    filter = "аеёиоуыэюяaeiou"

    result = []
    for char in text:
        char_low = char.lower()
        if char_low.isalpha():
            if char_low in filter:
                result.append(char.upper())
            else:
                result.append(char.lower())
        else:
            result.append(char)

    transformed_text = ''.join(result)
    print(f"результат преобразования: {transformed_text}")

