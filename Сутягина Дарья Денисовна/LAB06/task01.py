class Transport:
    def init(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity

    def info(self):
        return f"Скорость: {self.speed}\nВместимость: {self.capacity}"


class Bus(Transport):
    def init(self, speed, capacity, route_number):
        super().init(speed, capacity)
        self.route_number = route_number

    def info(self):
        base_info = super().info()
        return f"{base_info}\nНомер маршрута: {self.route_number}"


if __name__ == "__main__":
    transport = Transport(80, 4)
    bus = Bus(60, 40, 25)

    print("Информация о транспорте:")
    print(transport.info())

    print("\nИнформация об автобусе:")
    print(bus.info())

