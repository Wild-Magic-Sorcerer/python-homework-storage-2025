class Transport:
    def __init__(self, speed, capacity):
        self.__speed = speed
        self.__capacity = capacity
    def info(self):
        print(f"скорость: {self.__speed}, вместимость: {self.__capacity}")

class Bus(Transport):
    def __init__(self, speed, capacity, route_number):
        super().__init__(speed, capacity)
        self.__route_number = route_number
    def info(self):
        super().info()
        print(f"номер маршрута: {self.__route_number}")
        
if __name__ == "__main__":
    trans1 = Transport(10000, 5)
    bus1 = Bus(6, 400, 9)
    trans1.info()
    bus1.info()

