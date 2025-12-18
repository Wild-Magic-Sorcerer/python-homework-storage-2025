#!/usr/bin/env python3
"""CLI: копирование файла. Пример: python task_04.py -i src.txt -o dst.txt"""

import argparse
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Копирование")
    parser.add_argument("-i", "--input", required=True, dest="src")
    parser.add_argument("-o", "--output", required=True, dest="dst")
    args = parser.parse_args()
    
    src, dst = Path(args.src), Path(args.dst)
    if not src.exists():
        print(f"Файл не найден: {src}", file=sys.stderr)
        return 1
    
    dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"OK: {src} -> {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
