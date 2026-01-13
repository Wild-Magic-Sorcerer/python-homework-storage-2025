import argparse

def main():
    parser = argparse.ArgumentParser(description="Программа для выполнения математических операций.")
    parser.add_argument('x', type=float, help='Первое число')
    parser.add_argument('y', type=float, help='Второе число')
    parser.add_argument('--operation', choices=['add', 'sub', 'mul', 'div'], help='Тип операции')

    args = parser.parse_args()

    if args.operation is None:
        print(f"Числа: {args.x}, {args.y}")
    else:
        if args.operation == 'add':
            result = args.x + args.y
            print(f"Сумма: {result}")
        elif args.operation == 'sub':
            result = args.x - args.y
            print(f"Разность: {result}")
        elif args.operation == 'mul':
            result = args.x * args.y
            print(f"Произведение: {result}")
        elif args.operation == 'div':
            if args.y != 0:
                result = args.x / args.y
                print(f"Частное: {result}")
            else:
                print("Ошибка: Деление на ноль.")

if __name__ == "__main__":
    main()