import argparse


def factorial(numb, verbose=False):
    if not numb :
        return None

    res = 1
    for num in range(1, numb + 1):
        res *= num
        if verbose:
            print(f"Шаг {num}: {res}")

    print(f"Результат вычисления: {res}")
    return res
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int, help="Число для вычисления факториала")
    parser.add_argument("-v", "--verbose", action="store_true", help="Показать подробное вычисление")

    args = parser.parse_args()
    print(factorial(args.number, args.verbose))


