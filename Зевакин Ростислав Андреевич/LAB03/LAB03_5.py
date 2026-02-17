def factorial_recursive(n):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main():
    print("Вычисление факториала числа")

    while True:
        user_input = input("Введите целое неотрицательное число: ")
        try:
            number = int(user_input)

            if number < 0:
                print("Ошибка: факториал отрицательного числа не определен!")
                print("Введите неотрицательное число.")
                continue

            if number > 20:
                print(f"\nВнимание: Вы ввели большое число ({number})!")
                print("Факториал будет очень большим.")
                confirm = input("Дальше? (да/нет): ").lower()
                if confirm not in ['да', 'Да']:
                    print("Вычисления отменены.")
                    return
            break

        except ValueError:
            print(f"Ошибка: '{user_input}' не является целым числом!")
            print("Пожалуйста, введите целое число.")

    print(f"Вычисление факториала числа: {number}!")

    print("\n1. Рекурсивный метод:")
    try:
        if number > 1000:
            print("   Рекурсивный метод пропущен (слишком глубокий вызов)")
        else:
            result_rec = factorial_recursive(number)
            print(f"   {number}! = {result_rec}")
            print(f"   (Рекурсивных вызовов: {number})")
    except RecursionError:
        print("   Ошибка: превышена максимальная глубина рекурсии!")
    except Exception as e:
        print(f"   Ошибка: {e}")

    print("\n2. Итеративный метод:")
    try:
        result_iter = factorial_iterative(number)
        print(f"   {number}! = {result_iter}")
        print(f"   (Итераций цикла: {number if number > 0 else 0})")
    except Exception as e:
        print(f"   Ошибка: {e}")

    print("\n" + "-" * 50)
    if number <= 1000:
        try:
            rec_result = factorial_recursive(number)
            iter_result = factorial_iterative(number)
            if rec_result == iter_result:
                print("Результаты обоих методов совпадают!")
            else:
                print("Результаты методов различаются!")
        except:
            pass

if __name__ == "__main__":
    main()