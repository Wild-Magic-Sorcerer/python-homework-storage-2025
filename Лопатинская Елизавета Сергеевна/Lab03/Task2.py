def calculate_parity_sums(numbers):
    even_sum = 0
    odd_sum = 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return odd_sum, even_sum


if __name__ == "__main__":
    my_numbers = [10, 15, 22, 33, 40, 57, 60, 71]

    odds, evens = calculate_parity_sums(my_numbers)

    print("=" * 30)
    print(f"{'ИТОГИ ВЫЧИСЛЕНИЙ':^30}")
    print("=" * 30)
    print(f" Исходный список: {my_numbers}")
    print("-" * 30)
    print(f" Сумма чётных чисел:   {evens:>5}")
    print(f" Сумма нечётных чисел: {odds:>5}")
    print("=" * 30)
    