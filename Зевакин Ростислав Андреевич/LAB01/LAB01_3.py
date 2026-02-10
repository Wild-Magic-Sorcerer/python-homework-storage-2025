def main():
    user_words = input("Введите слова через пробел: ").strip()

    if not user_words:
        print("Не было введено ни одного слова")
        return

    words = user_words.split()

    unique_words_count = len(set(words))

    unique_words = set(words)

    print(f"Всего слов: {len(words)}")
    print(f"Количество уникальных слов: {unique_words_count}")
    print(f"Уникальные слова: {', '.join(sorted(unique_words))}")

if __name__ == "__main__":
    main()
