import string

def analyze_string(text):
    text_stripped = text.strip()
    results = {
        "words": 0,
        "letters": 0,
        "digits": 0,
        "spaces": 0,
        "punctuation": 0 }

    if text_stripped:
        results["words"] = len(text_stripped.split())

    for char in text:
        if char.isalpha():      # Проверка на букву
            results["letters"] += 1
        elif char.isdigit():    # Проверка на цифру
            results["digits"] += 1
        elif char.isspace():    # Проверка на пробел
            results["spaces"] += 1
        elif char in string.punctuation or char == "—":  # Проверка на пунктуацию
            results["punctuation"] += 1

    return results

def main():
    input_str = "    Привет, мир! Я правда не знаю что еще писать...    "
    analysis = analyze_string(input_str)
    print(f"Анализ строки: '{input_str}'")
    print("-" * 40)
    
    labels = {
        "words": "Слов",
        "letters": "Букв",
        "digits": "Цифр",
        "spaces": "Пробелов",
        "punctuation": "Знаков препинания" }

    for key, value in analysis.items():
        print(f"{labels[key]:<20}: {value}")

if __name__ == "__main__":
    main()


