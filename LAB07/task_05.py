#!/usr/bin/env python3
"""CLI: факториал с verbose. Пример: python task_05.py 5 --verbose"""

import argparse
import sys


def factorial(n: int, verbose: bool = False) -> int:
    """Факториал с опциональным выводом шагов."""
    result = 1
    if verbose:
        print(f"Вычисление {n}!:")
    for i in range(1, n + 1):
        result *= i
        if verbose:
            print(f"  {i}! = {result}")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Факториал")
    parser.add_argument("n", type=int)
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()
    
    if args.n < 0:
        print("n >= 0", file=sys.stderr)
        return 1
    
    result = factorial(args.n, args.verbose)
    if not args.verbose:
        print(f"{args.n}! = {result}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
