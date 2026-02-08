class Transport:
    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity

    def info(self):
        print(f"Скорость: {self.speed}")
        print(f"Вместимость: {self.capacity}")

class Bus(Transport):
    def __init__(self, speed, capacity, route_number):
        super().__init__(speed, capacity)
        self.route_number = route_number

    def info(self):
        super().info()
        print(f"Номер маршрута: {self.route_number}")

transport = Transport(80, 4)
bus = Bus(60, 40, 25)

print("Информация о транспорте:")
transport.info()

print("\nИнформация об автобусе:")
bus.info()
