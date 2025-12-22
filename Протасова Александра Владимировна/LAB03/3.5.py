def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    while True:
        try:
            number = int(input("Введите целое число для вычисления факториала: "))
            if number < 0:
                raise ValueError("Ошибка: Факториал определен только для неотрицательных чисел")
            break
        except ValueError as ve:
            print(ve)

    result_recursive = factorial_recursive(number)
    result_iterative = factorial_iterative(number)

    print(f"\n Факториал числа {number}:")
    print(f"Рекурсивный метод: {result_recursive}")
    print(f"Итеративный метод: {result_iterative}")

    if result_recursive == result_iterative:
        print("Результаты совпадают")
    else:
        print("Результаты не совпадают")
