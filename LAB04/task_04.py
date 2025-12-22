#!/usr/bin/env python3
import random

LOWER_BOUND = -20
UPPER_BOUND = 20
LIST_SIZE = 15
THRESHOLD = -5
RANDOM_SEED = 42


def main() -> None:
    random.seed(RANDOM_SEED)
    original_list = [random.randint(LOWER_BOUND, UPPER_BOUND) for _ in range(LIST_SIZE)]
    
    filter_condition = lambda num: num > THRESHOLD and num % 2 == 0
    filtered_list = list(filter(filter_condition, original_list))
    
    print(f"Исходный список: {original_list}")
    print(f"Отфильтрованные (чётные > {THRESHOLD}): {filtered_list}")


if __name__ == "__main__":
    main()
