#!/usr/bin/env python3

def process_text(input_string: str) -> tuple[str, ...]:
    if not input_string.strip():
        return tuple()
    return tuple(input_string.split())


def count_unique_words(word_tuple: tuple[str, ...]) -> int:
    return len(set(word_tuple))


def main() -> None:
    user_input = input("Введите слова, разделённые пробелами: ")
    words_tuple = process_text(user_input)
    
    if not words_tuple:
        print("Ошибка: введена пустая строка")
        return
    
    unique_count = count_unique_words(words_tuple)
    total_count = len(words_tuple)
    
    print(f"Кортеж слов: {words_tuple}")
    print(f"Всего слов: {total_count}")
    print(f"Уникальных слов: {unique_count}")


if __name__ == "__main__":
    main()
