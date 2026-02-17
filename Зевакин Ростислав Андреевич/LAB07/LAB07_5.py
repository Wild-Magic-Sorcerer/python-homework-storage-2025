import argparse


def main():
    parser = argparse.ArgumentParser(description='Вычисление факториала числа')
    parser.add_argument('number', type=int, help='Число для вычисления факториала')
    parser.add_argument('-v', '--verbose', action='store_true', help='Подробный режим вывода')

    args = parser.parse_args()

    if args.number < 0:
        print("Факториал отрицательного числа не определен")
        return

    result = 1
    process = []

    for i in range(1, args.number + 1):
        result *= i
        process.append(f"{i}")

    if args.verbose:
        print(" × ".join(process) + f" = {result}")
    else:
        print(result)


if __name__ == '__main__':
    main()