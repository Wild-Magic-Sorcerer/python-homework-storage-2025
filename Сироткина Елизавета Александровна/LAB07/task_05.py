#!/usr/bin/env python3
import argparse
import sys


def compute_factorial(value: int, detailed: bool = False) -> int:
    factorial_result = 1
    
    if detailed:
        print(f"Вычисление факториала {value}!:")
    
    for multiplier in range(1, value + 1):
        factorial_result *= multiplier
        if detailed:
            print(f"  {multiplier}! = {factorial_result}")
    
    return factorial_result


def main() -> int:
    parser = argparse.ArgumentParser(description="Вычисление факториала")
    parser.add_argument("n", type=int, help="Число для вычисления факториала")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Подробный режим с выводом промежуточных результатов",
    )
    args = parser.parse_args()
    
    if args.n < 0:
        print("Ошибка: число должно быть неотрицательным", file=sys.stderr)
        return 1
    
    result = compute_factorial(args.n, args.verbose)
    
    if not args.verbose:
        print(f"{args.n}! = {result}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
