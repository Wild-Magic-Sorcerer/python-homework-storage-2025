import string

def count_text_elements(text):

    counts = {
        "words": 0,
        "letters": 0,
        "digits": 0,
        "spaces": 0,
        "punctuation": 0
    }

    processed_text = text.strip()

    words = processed_text.split()
    counts["words"] = len(words)

    for char in processed_text:
        if char.isalpha():
            counts["letters"] += 1
        elif char.isdigit():
            counts["digits"] += 1
        elif char.isspace():
            counts["spaces"] += 1
        elif char in string.punctuation:
            counts["punctuation"] += 1

    return counts

if __name__ == "__main__":

    test_strings = []

    for i, text in enumerate(test_strings, 1):
        print(f"Тест {i}: '{text}'")
        result = count_text_elements(text)
        print(f"Результат: {result}")

    user_input = input("\nВведите строку для анализа (или нажмите Enter для выхода): ")
    while user_input:
        result = count_text_elements(user_input)
        print(f"Результат анализа: {result}")
        user_input = input("\nВведите строку для анализа (или нажмите Enter для выхода): ")

    print("Программа завершена.")
