user_words = input("Введите слова через пробел: ")

words_list = user_words.split()
words_tuple = tuple(words_list)


print(f"Кол-во уникальных слов: {len(set(words_tuple))}")
