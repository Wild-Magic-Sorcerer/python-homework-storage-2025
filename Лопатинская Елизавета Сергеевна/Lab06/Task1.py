class Transport:
    def __init__(self, speed, capacity):
        self.__speed = speed
        self.__capacity = capacity

    @property
    def speed(self):
        return self.__speed

    @property
    def capacity(self):
        return self.__capacity

    def info(self):
        print(f"Транспортное средство: Скорость = {self.__speed} км/ч, "
              f"Вместимость = {self.__capacity} чел.")

class Bus(Transport):
    def __init__(self, speed, capacity, route_number):
        super().__init__(speed, capacity)
        self.__route_number = route_number

    @property
    def route_number(self):
        return self.__route_number

    def info(self):
        print(f"Автобус (Маршрут №{self.__route_number}): "
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

    print("\n--- Попытка прямого доступа ---")
    try:
        print(city_bus.__speed)
    except AttributeError:
        print("Ошибка: Прямой доступ к '__speed' невозможен. Данные защищены!")

if __name__ == "__main__":
    main()
    
