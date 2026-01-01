import re

if __name__ == "__main__":
    text = input("Введите текст: ")
    parts = re.split(r"[\s.,!?—\-]+", text)
    result = []
    for item in parts:
        if item:
            result.append(item)
    print("Слова:", result)