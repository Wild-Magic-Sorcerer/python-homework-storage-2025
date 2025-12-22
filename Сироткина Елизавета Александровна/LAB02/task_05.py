#!/usr/bin/env python3
import string


def normalize_text(input_text: str) -> str:
    translator = str.maketrans("", "", string.punctuation)
    cleaned = input_text.translate(translator)
    return cleaned.lower()


def extract_word_set(normalized_text: str) -> set[str]:
    if not normalized_text.strip():
        return set()
    return set(normalized_text.split())


def find_differences(set1: set[str], set2: set[str]) -> tuple[set[str], set[str]]:
    only_in_first = set1 - set2
    only_in_second = set2 - set1
    return only_in_first, only_in_second


def display_comparison_result(
    first_only: set[str], second_only: set[str]
) -> None:
    if not first_only and not second_only:
        print("\nВсе слова присутствуют в обеих строках")
    else:
        if first_only:
            sorted_first = sorted(first_only)
            print(f"\nСлова только в первой строке: {', '.join(sorted_first)}")
        if second_only:
            sorted_second = sorted(second_only)
            print(f"Слова только во второй строке: {', '.join(sorted_second)}")


def main() -> None:
    first_input = input("Введите первую строку: ")
    second_input = input("Введите вторую строку: ")
    
    normalized_first = normalize_text(first_input)
    normalized_second = normalize_text(second_input)
    
    words_first = extract_word_set(normalized_first)
    words_second = extract_word_set(normalized_second)
    
    diff_first, diff_second = find_differences(words_first, words_second)
    display_comparison_result(diff_first, diff_second)


if __name__ == "__main__":
    main()
