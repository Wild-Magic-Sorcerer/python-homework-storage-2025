class Transport:
    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity
    def info(self):
        print(f"Скорость: {self.speed}, Вместимость: {self.capacity}")
class Bus(Transport):
    def __init__(self, speed, capacity, route_number):
        super().__init__(speed, capacity)
        self.route_number = route_number
    def info(self):
        super().info()
        print(f"Маршрут: {self.route_number}")
if __name__ == "__main__":
    t = Transport(85, 15)
    t.info()
    print()
    b = Bus(40, 18, 31)
    b.info()
