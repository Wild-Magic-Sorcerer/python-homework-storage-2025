def sum_num_odd(numbers):
    sum_even = 0
    sum_odd = 0
    for number in numbers:
        if number % 2 == 0:
            sum_even += number
        else:
            sum_odd += number
    return sum_even, sum_odd
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum, odd_sum = sum_num_odd(my_numbers)
print("Результаты расчета")
print(f"Сумма четных чисел:{even_sum}")
print(f"Сумма нечетных чисел:{odd_sum}")