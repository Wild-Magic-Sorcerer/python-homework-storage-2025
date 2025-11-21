def sum_odd_even(numbers):
    sum_odd = sum([num for num in numbers if num % 2 != 0])
    sum_even = sum([num for num in numbers if num % 2 == 0])
    return sum_odd, sum_even

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_sum, even_sum = sum_odd_even(numbers)
    print(f"Исходный список:{numbers}")
    print(f"Сумма нечётных чисел:{odd_sum}")
    print(f"Сумма чётных чисел:{even_sum}")
    print(f"Общая сумма:{odd_sum + even_sum}")

if __name__ == "__main__":
    main()

