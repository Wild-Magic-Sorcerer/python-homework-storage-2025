#!/usr/bin/env python3
"""Ввод 10 целых чисел и вычисление min/max/sum."""


def read_integers(count: int) -> list[int]:
    """Читает указанное количество целых чисел с валидацией."""
    result: list[int] = []
    while len(result) < count:
        try:
            value = int(input(f"Число ({count - len(result)} осталось): "))
            result.append(value)
        except ValueError:
            print("Некорректный ввод")
    return result


def main() -> None:
    numbers = read_integers(10)
    print(f"\nСписок: {numbers}")
    print(f"Min: {min(numbers)}, Max: {max(numbers)}, Sum: {sum(numbers)}")


if __name__ == "__main__":
    main()
