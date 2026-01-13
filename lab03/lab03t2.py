def sum_even_odd(numbers):
    sum_even = 0
    sum_odd = 0

    for number in numbers:
        if number % 2 == 0:
            sum_even += number
        else:
            sum_odd += number

    return sum_even, sum_odd


if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_sum, odd_sum = sum_even_odd(numbers)

    print(f"Сумма чётных чисел: {even_sum}")
    print(f"Сумма нечётных чисел: {odd_sum}")