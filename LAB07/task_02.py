#!/usr/bin/env python3
import argparse
import sys


def perform_operation(operand1: float, operand2: float, operation: str) -> float | None:
    operations = {
        "add": lambda a, b: a + b,
        "sub": lambda a, b: a - b,
        "mul": lambda a, b: a * b,
        "div": lambda a, b: a / b if b != 0 else None,
    }
    
    operation_symbols = {
        "add": "+",
        "sub": "-",
        "mul": "*",
        "div": "/",
    }
    
    if operation not in operations:
        return None
    
    return operations[operation](operand1, operand2)


def main() -> int:
    parser = argparse.ArgumentParser(description="Простой калькулятор")
    parser.add_argument("x", type=float, help="Первое число")
    parser.add_argument("y", type=float, help="Второе число")
    parser.add_argument(
        "-o",
        "--operation",
        choices=["add", "sub", "mul", "div"],
        help="Арифметическая операция",
    )
    args = parser.parse_args()
    
    if not args.operation:
        print(f"x = {args.x}, y = {args.y}")
        return 0
    
    result = perform_operation(args.x, args.y, args.operation)
    
    if result is None:
        print("Ошибка: деление на ноль", file=sys.stderr)
        return 1
    
    symbols = {"add": "+", "sub": "-", "mul": "*", "div": "/"}
    symbol = symbols[args.operation]
    print(f"{args.x} {symbol} {args.y} = {result}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
