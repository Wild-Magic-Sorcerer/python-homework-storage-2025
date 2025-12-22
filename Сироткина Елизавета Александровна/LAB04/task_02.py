#!/usr/bin/env python3

def main() -> None:
    word_list = ["apple", "banana", "cherry"]
    get_length = lambda text: len(text)
    length_list = list(map(get_length, word_list))
    
    print(f"Исходный список: {word_list}")
    print(f"Длины строк: {length_list}")


if __name__ == "__main__":
    main()
