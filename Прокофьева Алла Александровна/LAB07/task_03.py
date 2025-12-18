#!/usr/bin/env python3
"""CLI: список строк с подсчётом. Пример: python task_03.py a b c --count"""

import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description="Строки")
    parser.add_argument("strings", nargs="+")
    parser.add_argument("-c", "--count", action="store_true")
    args = parser.parse_args()
    
    if args.count:
        print(f"\nКоличество: {len(args.strings)}")
    else:
        for s in args.strings:
            print(s)
    return 0


if __name__ == "__main__":
    sys.exit(main())
