import argparse

def factorial(numb, verbose=False):
    if numb is None:
        return None

    res = 1
    process = [res := res * num for num in range(1, numb + 1)]

    if verbose:
        return f"Результат вычисления: {res}\nПодробное вычисление: {process}"
    else:
        return f"Результат вычисления: {res}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int, help="Число для вычисления факториала")
    parser.add_argument("-v", "--verbose", action="store_true", help="Показать подробное вычисление")

    args = parser.parse_args()

    result = factorial(args.number, args.verbose)
    print(result)