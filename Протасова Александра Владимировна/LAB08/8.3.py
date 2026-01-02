if __name__ == "__main__":
    text = input("Введите текст: ")

    punctuation = ".,!?-"

    for p in punctuation:
        text = text.replace(p, ' ')

    words = [word for word in text.split() if word]

    print("Список слов:")
    print(words)
