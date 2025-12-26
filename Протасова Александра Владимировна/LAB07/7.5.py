import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int)
    parser.add_argument("--verbose", "-v", action="store_true")

    args = parser.parse_args()

    if args.number < 0:
        print("Ошибка: факториал только для неотрицательных чисел")
        exit()

    result = 1
    if args.verbose:
        print(f"Вычисление факториала {args.number}!")

    for i in range(1, args.number + 1):
        result *= i
        if args.verbose:
            print(f"  {i}! = {result}")

    if args.verbose:
        print(f"\nРезультат: {args.number}! = {result}")
    else:
        print(f"{args.number}! = {result}")
