import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="вычисление факториала")
    parser.add_argument("number", type=int, help="число для вычисления факториала")
    parser.add_argument("-v", "--verbose", action="store_true", help="подробный режим вывода")
    args = parser.parse_args()

    result = 1

    if args.verbose:
        print("процесс вычисления:")
        current = 1
        for i in range(1, args.number + 1):
            current *= i
            print(f"{i}! = {current}")
        result = current
    else:
        for i in range(1, args.number + 1):
            result *= i

    print(f"итог:{args.number}! = {result}")
