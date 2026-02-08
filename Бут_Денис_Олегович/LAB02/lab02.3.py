
def transform_string(text):
    if not text:
        return None
    result = []

    vowels = "аеёиоуыэюяaeiou"

    for symb in text:
        symb_lower = symb.lower()

        if symb_lower.isalpha():
            if symb_lower in vowels:
                result.append(symb_lower.upper())
            else:
                result.append(symb_lower)
        else:
            result.append(symb)

    return "".join(result)

if __name__ == "__main__":
    string = "Некий русский текст! Some english text!"
    print(f"Исходная строка:, {string},\nПреобразованная: {transform_string(string)}")


