import string

def analyze_string(text):
    text = text.strip()

    results = {
        "words": 0,
        "letters": 0,
        "digits": 0,
        "spaces": 0,
        "punctuation": 0
    }

    if text:
        results["words"] = len(text.split())

    for char in text:
        if char.isalpha():  # Проверка на букву
            results["letters"] += 1
        elif char.isdigit():  # Проверка на цифру
            results["digits"] += 1
        elif char.isspace():  # Проверка на пробел
            results["spaces"] += 1
        elif char in string.punctuation or "—" in char:  # Проверка на пунктуацию
            results["punctuation"] += 1

    return results

input_str = "   Привет, мир! Я правда не знаю что еще писать...   "
analysis = analyze_string(input_str)

print(f"Анализ строки: '{input_str}'")
for key, value in analysis.items():
    print(f"{key.capitalize()}: {value}")
