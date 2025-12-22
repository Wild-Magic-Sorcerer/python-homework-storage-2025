#!/usr/bin/env python3
from functools import reduce

def main() -> None:
    number_sequence = list(range(1, 11))
    multiply = lambda x, y: x * y
    total_product = reduce(multiply, number_sequence)
    
    print(f"Исходный список: {number_sequence}")
    print(f"Произведение всех элементов: {total_product}")


if __name__ == "__main__":
    main()
