#!/usr/bin/env python3
"""Факториал: рекурсивная и итеративная реализация."""


def factorial_recursive(n: int) -> int:
    """Факториал рекурсивно."""
    if n < 0:
        raise ValueError("n >= 0")
    return 1 if n <= 1 else n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """Факториал итеративно."""
    if n < 0:
        raise ValueError("n >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main() -> None:
    while True:
        try:
            n = int(input("n (>= 0): "))
            if n >= 0:
                break
            print("Должно быть >= 0")
        except ValueError:
            print("Введите число")
    
    print(f"Рекурсивно: {factorial_recursive(n)}")
    print(f"Итеративно: {factorial_iterative(n)}")


if __name__ == "__main__":
    main()
