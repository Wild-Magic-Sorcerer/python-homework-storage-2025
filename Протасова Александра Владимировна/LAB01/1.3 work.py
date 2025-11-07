if __name__ == "__main__":
    input_string = input("Введите строку слов, разделённых пробелами: ")
    words_set = set(input_string.split())
    print(f"Количество уникальных слов: {len(words_set)}")
