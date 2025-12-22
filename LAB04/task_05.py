#!/usr/bin/env python3
from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")

BEFORE_MESSAGE = "Выполняется функция..."
AFTER_MESSAGE = "Функция выполнена."


def execution_logger(func: Callable[..., T]) -> Callable[..., T]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> T:
        print(BEFORE_MESSAGE)
        function_result = func(*args, **kwargs)
        print(AFTER_MESSAGE)
        return function_result
    
    return wrapper


@execution_logger
def compute_square(value: int | float) -> int | float:
    return value * value


def main() -> None:
    test_values = [5, 7, 2.5]
    
    for test_val in test_values:
        print(f"\ncompute_square({test_val}) = {compute_square(test_val)}")


if __name__ == "__main__":
    main()
