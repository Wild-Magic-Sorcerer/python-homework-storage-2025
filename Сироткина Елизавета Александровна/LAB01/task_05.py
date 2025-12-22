#!/usr/bin/env python3
import random

MIN_VALUE = -10
MAX_VALUE = 10
LIST_SIZE = 20
DIVISOR = 3


def generate_random_list(size: int, min_val: int, max_val: int) -> list[int]:
    return [random.randint(min_val, max_val) for _ in range(size)]


def filter_divisible(numbers: list[int], divisor: int) -> list[int]:
    return [num for num in numbers if num % divisor == 0]


def main() -> None:
    original_list = generate_random_list(LIST_SIZE, MIN_VALUE, MAX_VALUE)
    filtered_list = filter_divisible(original_list, DIVISOR)
    
    print(f"Исходный список: {original_list}")
    print(f"Числа, кратные {DIVISOR}: {filtered_list}")


if __name__ == "__main__":
    main()
