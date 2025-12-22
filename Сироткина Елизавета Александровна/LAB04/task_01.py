#!/usr/bin/env python3

def main() -> None:
    check_parity = lambda number: number % 2 == 0
    
    start_range = 1
    end_range = 11
    
    print(f"Проверка чётности чисел от {start_range} до {end_range - 1}:")
    for num in range(start_range, end_range):
        parity_status = "чётное" if check_parity(num) else "нечётное"
        print(f"  {num}: {parity_status}")


if __name__ == "__main__":
    main()
