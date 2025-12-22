#!/usr/bin/env python3
import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Выводит приветствие с указанным именем"
    )
    parser.add_argument("name", help="Имя пользователя для приветствия")
    args = parser.parse_args()
    
    print(f"Привет, {args.name}!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
