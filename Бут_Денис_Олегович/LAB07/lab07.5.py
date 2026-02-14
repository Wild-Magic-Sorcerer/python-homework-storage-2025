import argparse


def factorial(numb, verbose=False):
    if not numb :
        return None

    res = 1
    process = ""

    for num in range(1, numb + 1):
        res *= num
        if verbose:
            process += f"Шаг {num}: {res}\n"

    if verbose:
        return f"Результат вычисления: {res}\nПодробное вычисление:\n{process}"
    return f"Результат вычисления: {res}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int, help="Число для вычисления факториала")
    parser.add_argument("-v", "--verbose", action="store_true", help="Показать подробное вычисление")

    args = parser.parse_args()
    print(factorial(args.number, args.verbose))


