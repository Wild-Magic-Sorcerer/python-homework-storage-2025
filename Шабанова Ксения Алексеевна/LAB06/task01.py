def main():
    class Transport:
        def __init__(self, speed, capacity):
            self.speed = speed
            self.capacity = capacity
    
        def info(self):
            print(f"Транспорт: скорость {self.speed} км/ч, вместимость {self.capacity} чел.")
    
    class Bus(Transport):
        def __init__(self, speed, capacity, route_number):
            super().__init__(speed, capacity)
            self.route_number = route_number
    
        def info(self):
            # Переопределяем метод
            print(f"Автобус №{self.route_number}: скорость {self.speed} км/ч, вместимость {self.capacity} чел.")
    
    # Проверка
    t = Transport(120, 50)
    b = Bus(80, 40, "294")
    
    t.info()
    
    b.info()

if __name__ == "__main__":
    main()
    
