class Transport:
    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity
    def info(self):
        print(f"скорость: {self.speed}, вместимость: {self.capacity}")

class Bus(Transport):
    def __init__(self, speed, capacity, route_number):
        super().__init__(speed, capacity)
        self.route_number = route_number
    def info(self):
        super().info()
        print(f"номер маршрута: {self.route_number}")

trans1 = Transport(10000, 5)
bus1 = Bus(6, 400, 9)
trans1.info()
bus1.info()
