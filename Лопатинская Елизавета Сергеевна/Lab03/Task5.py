def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def main():
    user_input = input("Введите целое неотрицательное число для вычисления факториала: ")

    try:
        number = int(user_input)

        if number < 0:
            print("Ошибка: Факториал определен только для неотрицательных чисел.")
        else:
            res_iter = factorial_iterative(number)
            res_recur = factorial_recursive(number)

            print("-" * 30)
            print(f"Результат (итеративно): {res_iter}")
            print(f"Результат (рекурсивно): {res_recur}")
            print("-" * 30)

            if res_iter == res_recur:
                print("Оба метода вернули одинаковый результат.")

    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное целое число.")


if __name__ == "__main__":
    main()
    
