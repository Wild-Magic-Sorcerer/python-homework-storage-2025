from collections import Counter


def count_occurrences(numbers: list) -> dict:

    return dict(Counter(numbers))


def print_results(occurrences: dict) -> None:
    print("Статистика повторений чисел:")

    for number, count in sorted(occurrences.items()):
        print(f"Число {number} встречается {count} раз(а)")

    total_numbers = sum(occurrences.values())
    unique_numbers = len(occurrences)
    print(f"Всего чисел: {total_numbers}")
    print(f"Уникальных чисел: {unique_numbers}")

    if occurrences:
        most_common = max(occurrences.items(), key=lambda x: x[1])
        print(f"Наиболее часто встречается: {most_common[0]} "
              f"({most_common[1]} раз(а))")


def main() -> None:
    NUMBERS = [1, 2, 3, 4, 5, 6, 7, 2, 1, 3, 7, 4, 2, 5, 7,
               1, 3, 6, 2, 4, 1, 6, 5, 4, 3, 2, 1]

    print("Анализ списка чисел:")
    print(f"Список: {NUMBERS}")
    print()

    occurrences = count_occurrences(NUMBERS)
    print_results(occurrences)


if __name__ == "__main__":
    main()
