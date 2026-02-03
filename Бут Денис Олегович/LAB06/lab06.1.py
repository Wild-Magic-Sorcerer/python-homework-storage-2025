class Transport:
    def __init__(self, speed, capacity):
        self._speed = speed
        self._capacity = capacity

    def info(self):
        print(f"Скорость транспорта:{self._speed}, мощность транспорта:{self._capacity}")


class Bus(Transport):
    def __init__(self, speed, capacity, route_number):
        super().__init__(speed, capacity)
        self.__route_number = route_number

    def info(self):

        print(f"Скорость транспорта:{self._speed}, мощность транспорта:{self._capacity}")
        print(f"Маршрут транспорта:{self.__route_number}")

if __name__ == '__main__':
    Plane = Transport(200, 67)
    Plane.info()

    Some_bus = Bus(120, 28, 2)
    Some_bus.info()

