import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: --verbose")
        sys.exit(1)

    verbose = '--verbose' in sys.argv

    number = None
    for arg in sys.argv[1:]:
        if arg != '--verbose':
            try:
                number = int(arg)
                break
            except ValueError:
                pass

    if number is None:
        print("Ошибка: не указано число")
        sys.exit(1)

    if number < 0:
        print("Ошибка: факториал определен только для неотрицательных чисел")
        sys.exit(1)

    result = 1
    if verbose:
        print(f"Вычисление факториала {number}!")

    for i in range(1, number + 1):
        result *= i
        if verbose:
            print(f"  {i}! = {result}")

    if verbose:
        print(f"\nРезультат: {number}! = {result}")
    else:
        print(f"{number}! = {result}")
