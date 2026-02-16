def count_unique_words():
    user_input = input("Введите слова, разделённые пробелами: ")

    words_tuple = tuple(user_input.split())

    unique_count = len(set(words_tuple))

    print(f"Ваш кортеж: {words_tuple}")
    print(f"Количество уникальных слов: {unique_count}")


if __name__ == "__main__":
    count_unique_words()

