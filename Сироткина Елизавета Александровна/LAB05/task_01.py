#!/usr/bin/env python3
import random
from pathlib import Path

NUMBERS_FILE = Path(__file__).parent / "numbers.txt"
NUMBER_COUNT = 10
MIN_VALUE = 1
MAX_VALUE = 100


def generate_number_file(file_path: Path, number_count: int) -> list[int]:
    generated_numbers = [
        random.randint(MIN_VALUE, MAX_VALUE) for _ in range(number_count)
    ]
    file_path.write_text("\n".join(map(str, generated_numbers)), encoding="utf-8")
    return generated_numbers


def load_numbers_from_file(file_path: Path) -> list[int]:
    file_content = file_path.read_text(encoding="utf-8")
    return [int(num_str) for num_str in file_content.split() if num_str.strip()]


def calculate_statistics(number_list: list[int]) -> tuple[int, int, float]:
    if not number_list:
        raise ValueError("Список чисел не может быть пустым")
    return min(number_list), max(number_list), sum(number_list) / len(number_list)


def main() -> None:
    generated = generate_number_file(NUMBERS_FILE, NUMBER_COUNT)
    print(f"Сгенерированные числа: {generated}")
    
    loaded_numbers = load_numbers_from_file(NUMBERS_FILE)
    minimum, maximum, average = calculate_statistics(loaded_numbers)
    
    print(f"Минимум: {minimum}")
    print(f"Максимум: {maximum}")
    print(f"Среднее: {average:.1f}")


if __name__ == "__main__":
    main()
