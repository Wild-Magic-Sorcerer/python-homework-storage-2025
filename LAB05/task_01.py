#!/usr/bin/env python3
"""Чтение чисел из файла и вычисление min/max/avg."""

import random
from pathlib import Path

DATA_FILE = Path(__file__).parent / "numbers.txt"


def create_file(path: Path, count: int = 10) -> list[int]:
    """Создаёт файл со случайными числами."""
    nums = [random.randint(1, 100) for _ in range(count)]
    path.write_text("\n".join(map(str, nums)), encoding="utf-8")
    return nums


def read_file(path: Path) -> list[int]:
    """Читает числа из файла."""
    text = path.read_text(encoding="utf-8")
    return [int(x) for x in text.split() if x]


def main() -> None:
    nums = create_file(DATA_FILE)
    print(f"Файл: {nums}")
    
    data = read_file(DATA_FILE)
    print(f"Min: {min(data)}, Max: {max(data)}, Avg: {sum(data)/len(data):.1f}")


if __name__ == "__main__":
    main()
