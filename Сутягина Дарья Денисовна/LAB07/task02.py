import argparse

parser = argparse.ArgumentParser(description="Простые математические операции")

parser.add_argument("x", type=float, help="Первое число")
parser.add_argument("y", type=float, help="Второе число")

parser.add_argument(
    "--op",
    choices=["add", "sub", "mul", "div"],
    help="Математическая операция"
)

args = parser.parse_args()

x = args.x
y = args.y

if args.op is None:
    print("Введённые числа:", x, y)
elif args.op == "add":
    print("Результат сложения:", x + y)
elif args.op == "sub":
    print("Результат вычитания:", x - y)
elif args.op == "mul":
    print("Результат умножения:", x * y)
elif args.op == "div":
    if y == 0:
        print("Ошибка: делить на ноль нельзя")
    else:
        print("Результат деления:", x / y)
