import argparse


def calculate(num1, num2, operation=None):

    if operation is None:
        return f"Ваши числа: {num1}, {num2}"

    if operation == "add":
        res = num1 + num2
        op_symbol = "+"
    elif operation == "sub":
        res = num1 - num2
        op_symbol = "-"
    elif operation == "mul":
        res = num1 * num2
        op_symbol = "*"
    elif operation == "div":
        if num2 == 0:
            return "Ошибка: деление на ноль"
        res = num1 / num2
        op_symbol = "/"
    else:
        return "Ошибка: некорректная операция"

    return f"Результат: {num1} {op_symbol} {num2} = {res}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("num1", type=int, help="Первое число")
    parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Операция: add(+), sub(-), mul(*), div(/)")
    parser.add_argument("num2", type=int, help="Второе число")

    args = parser.parse_args()

    result = calculate(args.num1, args.num2, args.operation)
    print(result)
