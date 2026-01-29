import re

if __name__ == "__main__":
    text = input("Введите текст: ")
    parts = re.split(r"[\s.,!?—\-]+", text)
    result = [item.strip() for item in parts if item]
    print("Слова:", result)

