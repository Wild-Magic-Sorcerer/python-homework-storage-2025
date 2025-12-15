import sys

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) < 2:
        print("Ошибка: нужно передать два числа.")
        sys.exit(1)

    try:
        x = float(args[0])
        y = float(args[1])
    except ValueError:
        print("Ошибка: оба аргумента должны быть числами.")
        sys.exit(1)

    if len(args) >= 3:
        operation = args[2]

        if operation == 'add':
            print(f"{x} + {y} = {x + y}")
        elif operation == 'sub':
            print(f"{x} - {y} = {x - y}")
        elif operation == 'mul':
            print(f"{x} * {y} = {x * y}")
        elif operation == 'div':
            if y == 0:
                print("Ошибка: деление на ноль!")
            else:
                print(f"{x} / {y} = {x / y}")
        else:
            print(f"Неизвестная операция '{operation}'. x = {x}, y = {y}")
    else:
        print(f"x = {x}, y = {y}")
