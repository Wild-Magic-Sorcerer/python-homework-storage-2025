#!/usr/bin/env python3
from typing import Any

def is_valid_integer(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def multiply_integer_args(*arguments: Any) -> int | None:
    integer_values = [arg for arg in arguments if is_valid_integer(arg)]
    
    if not integer_values:
        return None
    
    product = 1
    for value in integer_values:
        product *= value
    
    return product


def main() -> None:
    test_cases = [
        (1, 2, 3, 4),
        (1, "x", 2, 3.14, 4),
        ("a", 3.14, [1]),
        (True, 5, 10),
        (),
    ]
    
    for test_args in test_cases:
        result = multiply_integer_args(*test_args)
        print(f"{test_args} -> {result}")


if __name__ == "__main__":
    main()
