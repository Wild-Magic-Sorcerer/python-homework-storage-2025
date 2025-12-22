#!/usr/bin/env python3

class Transport:
    def __init__(self, speed: float, capacity: int) -> None:
        self.speed = speed
        self.capacity = capacity
    
    def info(self) -> None:
        print(f"Скорость: {self.speed} км/ч, вместимость: {self.capacity}")


class Bus(Transport):
    def __init__(self, speed: float, capacity: int, route: str) -> None:
        super().__init__(speed, capacity)
        self.route = route
    
    def info(self) -> None:
        print(
            f"Автобус маршрута {self.route}: "
            f"скорость {self.speed} км/ч, мест {self.capacity}"
        )


def main() -> None:
    transport = Transport(speed=60.0, capacity=4)
    bus = Bus(speed=50.0, capacity=40, route="42")
    
    transport.info()
    bus.info()


if __name__ == "__main__":
    main()
