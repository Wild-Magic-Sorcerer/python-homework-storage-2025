import argparse
import sys

def calculate_factorial(n, verbose=False):
    if n < 0:
        return "Ошибка: факториал отрицательного числа не определен."
    if n == 0 or n == 1:
        if verbose:
            print(f"Факториал {n} по определению равен 1.")
        return 1

    result = 1
    if verbose:
        print(f"Начинаем вычисление факториала для числа {n}:")

    for i in range(1, n + 1):
        old_result = result
        result *= i
        if verbose:
            print(f"Шаг {i}: {old_result} * {i} = {result}")

    return result


def main():
    parser = argparse.ArgumentParser(description="Вычисление факториала с подробным режимом")

    parser.add_argument("number", type=int, help="Число, факториал которого нужно найти")

    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Показать подробный процесс вычисления")

    args = parser.parse_args()

    try:
        res = calculate_factorial(args.number, args.verbose)
        print(f"\nИтоговый результат: {res}")
    except Exception as e:
        print(f"Произошла ошибка: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()

