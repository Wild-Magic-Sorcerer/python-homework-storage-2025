#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path


def copy_file(source_path: Path, destination_path: Path) -> bool:
    if not source_path.exists():
        return False
    
    file_content = source_path.read_text(encoding="utf-8")
    destination_path.write_text(file_content, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Копирование файла")
    parser.add_argument(
        "-i", "--input", required=True, dest="src", help="Путь к исходному файлу"
    )
    parser.add_argument(
        "-o", "--output", required=True, dest="dst", help="Путь к целевому файлу"
    )
    args = parser.parse_args()
    
    source = Path(args.src)
    destination = Path(args.dst)
    
    if not copy_file(source, destination):
        print(f"Ошибка: файл не найден: {source}", file=sys.stderr)
        return 1
    
    print(f"Успешно: {source} -> {destination}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
