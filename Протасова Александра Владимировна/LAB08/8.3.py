import re

if __name__ == "__main__":
    text = input("Введите текст: ")

    words = re.split(r'[.,!?-]', text)

    words = [word for word in words if word]

    print("Список слов:")
    print(words)
