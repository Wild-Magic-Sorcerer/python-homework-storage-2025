if __name__ == '__main__':
    str_words = input("Введите пожалуйста слова через пробел:\n")
    words_tuple = tuple(str_words.split(" "))
    words_set = set(str_words.split(" "))

    print(f"Количество уникальных слов в строке: {len(words_set)}")

