#!/usr/bin/env python3
DATA_SET = [1, 3, 5, 3, 7, 1, 9, 3, 5, 1, 2, 8, 5, 3, 1, 7, 2, 9, 1]


def analyze_frequency(values: list[int]) -> dict[int, int]:
    frequency_map: dict[int, int] = {}
    for value in values:
        if value in frequency_map:
            frequency_map[value] += 1
        else:
            frequency_map[value] = 1
    return frequency_map


def display_results(frequency_data: dict[int, int]) -> None:
    sorted_keys = sorted(frequency_data.keys())
    for key in sorted_keys:
        count = frequency_data[key]
        print(f"{key} — {count}")
    print(f"\nВсего уникальных значений: {len(frequency_data)}")


def main() -> None:
    print(f"Исходный список: {DATA_SET}\n")
    frequency = analyze_frequency(DATA_SET)
    display_results(frequency)


if __name__ == "__main__":
    main()
