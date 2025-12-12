class Transport:
    def __init__(self, speed, capacity):
        self._speed = speed
        self._capacity = capacity

    @property
    def speed(self):
        return self._speed

    @property
    def capacity(self):
        return self._capacity

    def info (self):
        print(f'Скорость транспорта: {self.speed}')
        print(f'Мощьность транспорта: {self.capacity}')

class Bus(Transport):
    def __init__(self, speed, capacity,route_number):
        super().__init__(speed, capacity)
        self.__route_number = route_number

    @property
    def route_number(self):
        return self.__route_number

    def info(self):
        print(f'Скорость автобуса: {self.speed} км/ч')
        print(f'Мощьность автобуса: {self.capacity} лошадиных сил')
        print(f'Автобус следует моршруту № {self.route_number}')
        return None

if __name__ == '__main__':
    speed_avto = input(f'Введите скорость транспорта: ')
    speed_bus = input(f'Введите скорость автобуса: ')
    capacity_avto = input(f'Введите мощность транспорта: ')
    capacity_bus = input(f'Введите мощность автобуса: ')
    route_number_bus = input(f'Введите номер маршрута: ')

    avto = Transport(speed_avto, capacity_avto)
    bus = Bus(speed_bus, capacity_bus, route_number_bus)

    avto.info()
    bus.info()
