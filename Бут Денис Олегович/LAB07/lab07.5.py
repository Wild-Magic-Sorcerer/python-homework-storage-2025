import argparse

def factorial(args_object):
    if args_object.number is None:
        return None
    n = args_object.number

    result = 1
    process = [result := result * num for num in range(1, n + 1)]

    if args_object.verbose:
        return f"Результат вычисления: {result}\nПодробное вычисление: {process}"
    else:
        return f"Результат вычисления: {result}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int, help="Число для вычисления факториала")
    parser.add_argument("-v", "--verbose", action="store_true", help="Показать подробное вычисление")

    args = parser.parse_args()
    print(factorial(args))

