#!/usr/bin/env python3
"""Классы Transport и Bus с наследованием."""


class Transport:
    """Базовый транспорт."""
    
    def __init__(self, speed: float, capacity: int) -> None:
        self.speed = speed
        self.capacity = capacity
    
    def info(self) -> None:
        print(f"Скорость: {self.speed} км/ч, вместимость: {self.capacity}")


class Bus(Transport):
    """Автобус с маршрутом."""
    
    def __init__(self, speed: float, capacity: int, route: str) -> None:
        super().__init__(speed, capacity)
        self.route = route
    
    def info(self) -> None:
        print(f"Автобус {self.route}: {self.speed} км/ч, мест: {self.capacity}")


def main() -> None:
    t = Transport(60, 4)
    b = Bus(50, 40, "42")
    
    t.info()
    b.info()


if __name__ == "__main__":
    main()
