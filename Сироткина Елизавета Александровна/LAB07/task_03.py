#!/usr/bin/env python3
import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description="Обработка списка строк")
    parser.add_argument("strings", nargs="+", help="Список строк для обработки")
    parser.add_argument(
        "-c", "--count", action="store_true", help="Вывести количество строк"
    )
    args = parser.parse_args()
    
    if args.count:
        print(f"Количество строк: {len(args.strings)}")
    else:
        for string_item in args.strings:
            print(string_item)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
