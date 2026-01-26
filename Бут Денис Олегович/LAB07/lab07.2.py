import argparse

def calculator(args_list):

    if args_list.num1 and args_list.operation and args_list.num2:
        num1, operation, num2 = args_list.num1, args_list.operation, args_list.num2

        operations = {
            "add": ("+", num1 + num2),
            "sub": ("-", num1 - num2),
            "mul": ("*", num1 * num2),
            "div": ("/", num1 / num2 if num2 != 0 else "деление на ноль"),
        }

        if operation in operations:
            op, res = operations[operation]
            return f" Результат вычислений = {res} "
        else:
            return "Ввод некорректной операции"

    elif args_list.num1 and args_list.num2:
        return f"Ваши числа: {args_list.num1}, {args_list.num2}"

    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Калькулятор")

    parser.add_argument("num1", nargs="?", type=int)
    parser.add_argument("num2", nargs="?", type=int)
    parser.add_argument("operation", nargs="?",
                        choices=["add", "sub", "mul", "div"])
    args = parser.parse_args()

    result = calculator(args)

