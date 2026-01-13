def main():
    input_string = input("Введите слова через пробел: ")
    words_tuple = tuple(input_string.split())
    unique_words = set(words_tuple)

    print(f"Ваш список слов: {words_tuple}")
    print(f"Количество уникальных слов в вашем списке: {len(unique_words)}")

if __name__ == "__main__":
    main()
  
