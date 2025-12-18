#!/usr/bin/env python3
"""Подсчёт вхождений чисел в списке."""

NUMBERS = [1, 3, 5, 3, 7, 1, 9, 3, 5, 1, 2, 8, 5, 3, 1, 7, 2, 9, 1]


def count_occurrences(numbers: list[int]) -> dict[int, int]:
    """Возвращает {число: кол-во вхождений}."""
    counts: dict[int, int] = {}
    for n in numbers:
        counts[n] = counts.get(n, 0) + 1
    return counts


def main() -> None:
    print(f"Список: {NUMBERS}\n")
    counts = count_occurrences(NUMBERS)
    
    for num in sorted(counts):
        print(f"  {num}: {counts[num]}")
    print(f"\nУникальных: {len(counts)}")


if __name__ == "__main__":
    main()
