class Transport:
    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity
    def info(self):
        return f"Скорость: {self.speed} км/ч, Вместимость: {self.capacity} человек"
class Bus(Transport):
    def __init__(self, speed, capacity, route_number):
        super().__init__(speed, capacity)
        self.route_number = route_number
    def info(self):
        return f"{super().info()}, Номер маршрута: {self.route_number}"

transport = Transport(60, 15)
print(transport.info())
bus = Bus(80, 50, 22)
print(bus.info())