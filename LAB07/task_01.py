#!/usr/bin/env python3
"""CLI: приветствие по имени. Пример: python task_01.py Алла"""

import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description="Приветствие")
    parser.add_argument("name", help="Имя")
    args = parser.parse_args()
    
    print(f"Привет, {args.name}!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
