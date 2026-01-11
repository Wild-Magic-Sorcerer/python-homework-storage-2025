class Transport:
    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity

    def info(self):
        print(f"Транспортное средство: Скорость = {self.speed} км/ч, "
              f"Вместимость = {self.capacity} чел.")

class Bus(Transport):
    def __init__(self, speed, capacity, route_number):
        super().__init__(speed, capacity)
        self.route_number = route_number

    def info(self):
        print(f"Автобус (Маршрут №{self.route_number}): "
              f"Скорость = {self.speed} км/ч, "
              f"Вместимость = {self.capacity} чел.")

def main():
    print("--- Тестирование системы транспорта ---")
    generic_transport = Transport(120, 5)
    print("Информация о базовом транспорте:")
    generic_transport.info()

    print("-" * 40)

    city_bus = Bus(60, 50, 42)
    print("Информация об автобусе:")
    city_bus.info()

if __name__ == "__main__":
    main()
    
