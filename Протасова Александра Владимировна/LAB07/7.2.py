import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=float)
    parser.add_argument("y", type=float)
    parser.add_argument("--operation", "-op", choices=["add", "sub", "mul", "div"])

    args = parser.parse_args()

    if args.operation is None:
        print(f"x = {args.x}, y = {args.y}")
    else:
        if args.operation == "add":
            print(f"{args.x} + {args.y} = {args.x + args.y}")
        elif args.operation == "sub":
            print(f"{args.x} - {args.y} = {args.x - args.y}")
        elif args.operation == "mul":
            print(f"{args.x} * {args.y} = {args.x * args.y}")
        elif args.operation == "div":
            if args.y == 0:
                print("Ошибка: деление на ноль!")
            else:
                print(f"{args.x} / {args.y} = {args.x / args.y}")
