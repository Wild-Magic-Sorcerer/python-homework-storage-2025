#!/usr/bin/env python3
"""Сумма чётных и нечётных чисел списка."""


def sum_odd_even(numbers: list[int]) -> tuple[int, int]:
    """Возвращает (сумма нечётных, сумма чётных)."""
    odd = sum(n for n in numbers if n % 2 != 0)
    even = sum(n for n in numbers if n % 2 == 0)
    return odd, even


def main() -> None:
    numbers = list(range(1, 16))
    odd, even = sum_odd_even(numbers)
    
    print(f"Список: {numbers}")
    print(f"Нечётные: {odd}, чётные: {even}")


if __name__ == "__main__":
    main()
