def ch_case(text: str) -> str:
    vowels = "аеёиоуыэюяaeiou"
    new_text = ""

    for symb in text:
        if symb.isalpha():
            if symb.lower() in vowels:
                new_text += symb.upper()
            else:
                new_text += symb.lower()
        else:
            new_text += symb

    return new_text


def main():
    user_text = input("Введите строку: ")
    result = ch_case(user_text)
    print("Результат:", result)


if __name__ == "__main__":
    main()
    
