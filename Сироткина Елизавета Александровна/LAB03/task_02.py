#!/usr/bin/env python3

def calculate_parity_sums(number_list: list[int]) -> tuple[int, int]:
    odd_sum = sum(num for num in number_list if num % 2 == 1)
    even_sum = sum(num for num in number_list if num % 2 == 0)
    return odd_sum, even_sum


def main() -> None:
    number_sequence = list(range(1, 16))
    sum_odd, sum_even = calculate_parity_sums(number_sequence)
    
    print(f"Исходный список: {number_sequence}")
    print(f"Сумма нечётных чисел: {sum_odd}")
    print(f"Сумма чётных чисел: {sum_even}")


if __name__ == "__main__":
    main()
