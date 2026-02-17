def sum_even_odd(numbers):
    sum_even = 0
    sum_odd = 0

    for num in numbers:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num

    return sum_even, sum_odd


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Тестовый список чисел

    even_sum, odd_sum = sum_even_odd(numbers)

    print("Анализ списка чисел")
    print(f"Список чисел: {numbers}")
    print(f"Сумма четных чисел:  {even_sum}")
    print(f"Сумма нечетных чисел: {odd_sum}")
    print(f"Общая сумма всех чисел: {even_sum + odd_sum}")

    print("Доп пример")
    numbers2 = [15, 22, 8, 3, 17, 6]
    even2, odd2 = sum_even_odd(numbers2)

    print(f"Список чисел: {numbers2}")
    print(f"Сумма четных чисел ({', '.join(str(n) for n in numbers2 if n % 2 == 0)}): {even2}")
    print(f"Сумма нечетных чисел ({', '.join(str(n) for n in numbers2 if n % 2 != 0)}): {odd2}")

if __name__ == "__main__":
    main()