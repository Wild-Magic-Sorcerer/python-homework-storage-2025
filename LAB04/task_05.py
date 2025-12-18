#!/usr/bin/env python3
"""Декоратор логирования выполнения функции."""

from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def log_execution(func: Callable[..., T]) -> Callable[..., T]:
    """Выводит сообщения до и после вызова."""
    @wraps(func)
    def wrapper(*args, **kwargs) -> T:
        print("Выполняется функция...")
        result = func(*args, **kwargs)
        print("Функция выполнена.")
        return result
    return wrapper


@log_execution
def square(n: int | float) -> int | float:
    """Квадрат числа."""
    return n * n


def main() -> None:
    for val in [5, 7, 2.5]:
        print(f"\nsquare({val}) = {square(val)}")


if __name__ == "__main__":
    main()
