#!/usr/bin/env python3
"""Lambda-функция для проверки чётности."""


def main() -> None:
    is_even = lambda x: x % 2 == 0
    
    print("Проверка 1-10:")
    for n in range(1, 11):
        print(f"  {n}: {'чёт' if is_even(n) else 'нечёт'}")


if __name__ == "__main__":
    main()
