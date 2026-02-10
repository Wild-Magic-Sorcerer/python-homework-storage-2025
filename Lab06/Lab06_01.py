# Создайте класс Transport, который содержит поля speed и capacity, а также метод info(), выводящий эти данные.
# Затем создайте класс Bus, наследующий Transport, который добавляет поле route_number и переопределяет метод info()
# чтобы он также выводил номер маршрута.
# Проверьте работу, создав по одному объекту каждого класса и вызвав их методы.

class Transport:
    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity

    def info(self):
        return f"Скорость транспортного средства: {self.speed}. Вместительность транспортного средства: {self.capacity}"

class Bus(Transport):
    def __int__(self, speed, capacity, route_number):
        super().__init__(speed, capacity)
        self.route_number = route_number

    def info(self):
        return f"{super().info()}, № маршрута: {self.route_number}"

car = Transport(50, 4)
bus = Bus(90, 25, 13)
print(car.info())
print(bus.info())
