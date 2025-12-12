if __name__ == "__main__":
    s = input("Введите слова через пробел: ").strip()

    words = s.split()
    words_tuple = tuple(words)

    low_list = []
    for w in words_tuple:
        low_list.append(w.lower())

    low = tuple(low_list)
    count = len(set(low))

    print("Кортеж:", words_tuple)
    print("Количество уникальных слов:", count)
