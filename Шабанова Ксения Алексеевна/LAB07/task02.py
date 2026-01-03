import argparse

parser = argparse.ArgumentParser()
parser.add_argument("x", type=float)
parser.add_argument("y", type=float)
parser.add_argument("--operation", choices=['add', 'sub', 'mul', 'div'], help="Операция")

args = parser.parse_args()

if args.operation == 'add':
    print(args.x + args.y)
elif args.operation == 'sub':
    print(args.x - args.y)
elif args.operation == 'mul':
    print(args.x * args.y)
elif args.operation == 'div':
    print(args.x / args.y if args.y != 0 else "Ошибка: деление на ноль")
else:
    print(f"Числа: {args.x}, {args.y}")