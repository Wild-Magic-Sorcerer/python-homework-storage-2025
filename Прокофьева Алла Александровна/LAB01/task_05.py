#!/usr/bin/env python3
"""Генератор списка с фильтрацией кратных 3."""

import random


def main() -> None:
    numbers = [random.randint(-10, 10) for _ in range(20)]
    divisible = [n for n in numbers if n % 3 == 0]
    
    print(f"Исходный: {numbers}")
    print(f"Кратные 3: {divisible}")


if __name__ == "__main__":
    main()
