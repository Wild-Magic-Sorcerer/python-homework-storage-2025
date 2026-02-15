input_string = input("Введите строку слов, разделенных пробелами: ").strip()

if not input_string:
    print("Вы ввели пустую строку!")
else:
    words_list = input_string.split()
    words_tuple = tuple(words_list)

    print(f"\nКортеж слов: {words_tuple}")
    print(f"Всего слов в кортеже: {len(words_tuple)}")

    unique_words = set(words_tuple)

    print(f"Количество уникальных слов: {len(unique_words)}")

    if len(unique_words) < len(words_tuple):
        print(f"Уникальные слова: {', '.join(sorted(unique_words))}")
