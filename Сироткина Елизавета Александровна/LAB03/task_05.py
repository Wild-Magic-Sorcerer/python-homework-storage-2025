#!/usr/bin/env python3

def compute_factorial_recursive(value: int) -> int:
    if value < 0:
        raise ValueError("Значение должно быть неотрицательным")
    if value <= 1:
        return 1
    return value * compute_factorial_recursive(value - 1)


def compute_factorial_iterative(value: int) -> int:
    if value < 0:
        raise ValueError("Значение должно быть неотрицательным")
    
    factorial_result = 1
    for multiplier in range(2, value + 1):
        factorial_result *= multiplier
    
    return factorial_result


def get_nonnegative_integer() -> int:
    while True:
        try:
            user_value = int(input("Введите неотрицательное целое число: "))
            if user_value >= 0:
                return user_value
            print("Ошибка: число должно быть неотрицательным")
        except ValueError:
            print("Ошибка: введите корректное целое число")


def main() -> None:
    number = get_nonnegative_integer()
    
    recursive_result = compute_factorial_recursive(number)
    iterative_result = compute_factorial_iterative(number)
    
    print(f"Факториал {number} (рекурсивно): {recursive_result}")
    print(f"Факториал {number} (итеративно): {iterative_result}")


if __name__ == "__main__":
    main()
