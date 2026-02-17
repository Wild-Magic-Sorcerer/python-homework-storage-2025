import argparse

parser = argparse.ArgumentParser(description="Простая математическая программа")
parser.add_argument("x", type=float, help="Первое число")
parser.add_argument("y", type=float, help="Второе число")
parser.add_argument(
    "--op",
    choices=["add", "sub", "mul", "div"],
    help="Математическая операция"
)

args = parser.parse_args()

x, y = args.x, args.y

if args.op is None:
    print(x, y)
elif args.op == "add":
    print(x + y)
elif args.op == "sub":
    print(x - y)
elif args.op == "mul":
    print(x * y)
elif args.op == "div":
    if y == 0:
        print("Ошибка: деление на ноль")
    else:
        print(x / y)

