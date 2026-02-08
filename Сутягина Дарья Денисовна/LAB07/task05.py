import argparse

parser = argparse.ArgumentParser(description="Вычисление факториала")

parser.add_argument(
    "number",
    type=int,
    help="Целое неотрицательное число"
)

parser.add_argument(
    "--verbose",
    action="store_true",
    help="Показать подробный процесс вычисления"
)

args = parser.parse_args()

n = args.number

if n < 0:
    print("Ошибка: число должно быть неотрицательным")
    exit()

result = 1

if args.verbose:
    print(f"Вычисление факториала числа {n}:")
    for i in range(1, n + 1):
        result *= i
        print(f"{i}! = {result}")
else:
    for i in range(1, n + 1):
        result *= i
    print(f"Факториал {n} = {result}")
