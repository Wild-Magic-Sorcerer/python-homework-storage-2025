import argparse

def main():

    parser = argparse.ArgumentParser(description="Калькулятор с двумя числами")
    parser.add_argument("x", type=float, help="Первое число")
    parser.add_argument("y", type=float, help="Второе число")
    parser.add_argument("--op",
                        choices=["add", "sub", "mul", "div"],
                        help="Математическая операция")

    args = parser.parse_args()
    if args.op is None:
        print(f"Числа: x = {args.x}, y = {args.y}")
    else:
        if args.op == "add":
            print(f"Результат: {args.x + args.y}")
        elif args.op == "sub":
            print(f"Результат: {args.x - args.y}")
        elif args.op == "mul":
            print(f"Результат: {args.x * args.y}")
        elif args.op == "div":
            if args.y != 0:
                print(f"Результат: {args.x / args.y}")
            else:
                print("Ошибка: деление на ноль!")

if __name__ == "__main__":
    main()
    
