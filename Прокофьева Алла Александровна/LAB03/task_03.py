#!/usr/bin/env python3
"""Произведение целочисленных аргументов из *args."""

from typing import Any


def multiply_integers(*args: Any) -> int | None:
    """Произведение int-аргументов. None если их нет. bool исключается."""
    ints = [a for a in args if isinstance(a, int) and not isinstance(a, bool)]
    if not ints:
        return None
    result = 1
    for n in ints:
        result *= n
    return result


def main() -> None:
    tests = [
        (1, 2, 3, 4),
        (1, "x", 2, 3.14, 4),
        ("a", 3.14, [1]),
        (True, 5, 10),
        (),
    ]
    for args in tests:
        print(f"{args} -> {multiply_integers(*args)}")


if __name__ == "__main__":
    main()
