#!/usr/bin/env python3
"""Использование reduce + lambda для произведения элементов."""

from functools import reduce


def main() -> None:
    numbers = list(range(1, 11))
    product = reduce(lambda a, b: a * b, numbers)
    
    print(f"Числа: {numbers}")
    print(f"Произведение: {product}")


if __name__ == "__main__":
    main()
