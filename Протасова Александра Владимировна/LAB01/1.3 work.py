# Задание 3
input_string = input("Введите строку слов, разделённых пробелами: ")
words_tuple = tuple(input_string.split())
unique_words = set(words_tuple)
print(f"Количество уникальных слов: {len(unique_words)}")