def main():
    input_string = input("Введите строку слов через пробелы: ")

    words_tuple = tuple(input_string.split())

    unique_words = set(words_tuple)
    unique_count = len(unique_words)

    print(f"\nКортеж слов: {words_tuple}")
    print(f"Количество уникальных слов: {unique_count}")

if __name__ == "__main__":
    main()
