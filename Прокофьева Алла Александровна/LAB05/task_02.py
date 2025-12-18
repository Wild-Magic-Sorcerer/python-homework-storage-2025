#!/usr/bin/env python3
"""Добавление строки в файл и вывод содержимого."""

from pathlib import Path

DATA_FILE = Path(__file__).parent / "strings.txt"


def main() -> None:
    DATA_FILE.touch(exist_ok=True)
    
    text = input("Строка: ")
    if not text.strip():
        print("Пусто")
        return
    
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")
    
    print("\nФайл:")
    for i, line in enumerate(DATA_FILE.read_text(encoding="utf-8").splitlines(), 1):
        print(f"  {i}. {line}")


if __name__ == "__main__":
    main()
