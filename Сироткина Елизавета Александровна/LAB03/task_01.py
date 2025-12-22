#!/usr/bin/env python3

def calculate_average_length(string_list: list[str]) -> float:
    if not string_list:
        return 0.0
    total_length = sum(len(s) for s in string_list)
    return total_length / len(string_list)


def filter_long_strings(string_list: list[str]) -> list[str]:
    if not string_list:
        return []
    
    average = calculate_average_length(string_list)
    return [s for s in string_list if len(s) > average]


def main() -> None:
    test_data = [
        "кот",
        "собака",
        "слон",
        "крокодил",
        "мышь",
        "бегемот",
        "лев",
        "жираф",
    ]
    
    average_length = calculate_average_length(test_data)
    filtered = filter_long_strings(test_data)
    
    print(f"Исходный список: {test_data}")
    print(f"Средняя длина строк: {average_length:.2f}")
    print(f"Строки длиннее средней: {filtered}")


if __name__ == "__main__":
    main()
