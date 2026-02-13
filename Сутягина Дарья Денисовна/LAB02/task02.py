def analyze_string(text: str) -> dict:
    text = text.strip()

    result = {
        "words": 0,
        "letters": 0,
        "digits": 0,
        "spaces": 0,
        "punctuation": 0
    }

    if text:
        result["words"] = len(text.split())

    punctuation_marks = ".,!?;:-()\"'"

    for char in text:
        if char.isalpha():
            result["letters"] += 1
        elif char.isdigit():
            result["digits"] += 1
        elif char == " ":
            result["spaces"] += 1
        elif char in punctuation_marks:
            result["punctuation"] += 1

    return result

if __name__ == "__main__":
    user_input = input("Введите строку: ")
    res = analyze_string(user_input)

    print("Количество слов:", res["words"])
    print("Количество букв:", res["letters"])
    print("Количество цифр:", res["digits"])
    print("Количество пробелов:", res["spaces"])
    print("Количество знаков препинания:", res["punctuation"])
