#!/usr/bin/env python3
"""Использование filter + lambda: чётные числа больше -5."""

import random


def main() -> None:
    random.seed(42)
    numbers = [random.randint(-20, 20) for _ in range(15)]
    
    filtered = list(filter(lambda x: x > -5 and x % 2 == 0, numbers))
    
    print(f"Исходный: {numbers}")
    print(f"Чётные > -5: {filtered}")


if __name__ == "__main__":
    main()
