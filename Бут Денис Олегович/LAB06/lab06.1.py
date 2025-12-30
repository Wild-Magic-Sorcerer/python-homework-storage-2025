class Transport:

    def __init__(self,speed,capacity):
        self.speed = speed
        self.capacity = capacity

    def info(self):
        print(f"Скорость транспорта:{self.speed}, мощность транспорта:{self.capacity}")

class Bus(Transport):

    def __init__(self,speed,capacity,route_number):
        super().__init__(speed,capacity)
        self.route_number = route_number

    def info(self):
        print(f"Маршрут транспорта:{self.route_number}")
        print(f"Скорость транспорта:{self.speed}, мощность транспорта:{self.capacity}")

if __name__ == '__main__':
    Plane = Transport(200,67)
    Plane.info()
    Some_bus = Bus(120,28,2)
    Some_bus.info()