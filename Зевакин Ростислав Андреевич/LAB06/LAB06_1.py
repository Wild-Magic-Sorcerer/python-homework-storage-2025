class Transport:

    def __init__(self, speed, capacity):

        self.speed = speed
        self.capacity = capacity

    def info(self):
        print(f"Скорость: {self.speed} км/ч")
        print(f"Вместимость: {self.capacity} человек")


class Bus(Transport):

    def __init__(self, speed, capacity, route_number):
        super().__init__(speed, capacity)

        self.route_number = route_number

    def info(self):
        super().info()
        print(f"Номер маршрута: {self.route_number}")


def main():
    print("Работа классов TRANSPORT И BUS")

    print("1. Создание объекта класса TRANSPORT:")

    car = Transport(speed=120, capacity=4)
    print("Создан объект класса Transport:")
    print(f"  Тип объекта: {type(car).__name__}")
    print(f"  Скорость: {car.speed} км/ч")
    print(f"  Вместимость: {car.capacity} человек")

    print("Вызов метода info():")
    car.info()

    print("2. Создание объекта класса BUS:")

    bus = Bus(speed=80, capacity=55, route_number=363)
    print("Создан объект класса Bus:")
    print(f" Тип объекта: {type(bus).__name__}")
    print(f" Скорость: {bus.speed} км/ч")
    print(f" Вместимость: {bus.capacity} человек")
    print(f" Номер маршрута: {bus.route_number}")

    print("Вызов метода info():")
    bus.info()

    print("3. Ещё одна демонстрация:")

    transports = [
        Transport(speed=220, capacity=1),  # Мотоцикл
        Bus(speed=70, capacity=80, route_number="545-А"),  # Большой автобус
        Bus(speed=80, capacity=30, route_number=545),  # Маршрутка
        Transport(speed=150, capacity=4)  # Легковая машина
    ]

    print("Список всех транспортных средств:")
    for i, transport in enumerate(transports, 1):
        print(f"\n{i}. {type(transport).__name__}:")
        transport.info()

    print("4. Работа транспорта:")

    print("Изменение полей объектов:")

    print(f"\nДо изменения:")
    bus.info()

    bus.speed = 70
    bus.capacity = 40
    bus.route_number = "363А"

    print(f"После изменения:")
    bus.info()

    print("5. Проверка принадлежности к классам:")

    print(f"car является Transport: {isinstance(car, Transport)}")
    print(f"car является Bus: {isinstance(car, Bus)}")
    print(f"bus является Transport: {isinstance(bus, Transport)}")
    print(f"bus является Bus: {isinstance(bus, Bus)}")

if __name__ == "__main__":
    main()