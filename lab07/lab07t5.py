import sys

def factorial(n, verbose=False):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1

    result = 1
    if verbose:
        print(f"Вычисляем факториал числа {n}:")

    for i in range(2, n + 1):
        result *= i
        if verbose:
            print(f"{i}! = {result}")

    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python factorial.py <число> [--verbose]")
        sys.exit(1)

    number = int(sys.argv[1])
    verbose_mode = "--verbose" in sys.argv

    result = factorial(number, verbose_mode)

    if result is not None:
        print(f"Факториал числа {number} равен {result}.")
    else:
        print("Ошибка: факториал отрицательного числа не определён.")