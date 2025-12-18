#!/usr/bin/env python3
"""CLI: калькулятор. Пример: python task_02.py 10 5 -o mul"""

import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description="Калькулятор")
    parser.add_argument("x", type=float)
    parser.add_argument("y", type=float)
    parser.add_argument("-o", "--operation", choices=["add", "sub", "mul", "div"])
    args = parser.parse_args()
    
    if not args.operation:
        print(f"x={args.x}, y={args.y}")
        return 0
    
    ops = {
        "add": ("+", lambda a, b: a + b),
        "sub": ("-", lambda a, b: a - b),
        "mul": ("*", lambda a, b: a * b),
        "div": ("/", lambda a, b: a / b if b else None),
    }
    sym, fn = ops[args.operation]
    result = fn(args.x, args.y)
    
    if result is None:
        print("Деление на ноль", file=sys.stderr)
        return 1
    
    print(f"{args.x} {sym} {args.y} = {result}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
