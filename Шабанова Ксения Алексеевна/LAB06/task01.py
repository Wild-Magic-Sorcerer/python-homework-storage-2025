class Transport:
    def __init__(self, speed, capacity):
        self.__speed = speed
        self.__capacity = capacity

    def info(self):
        print(f"Транспорт: скорость {self.__speed} км/ч, вместимость {self.__capacity} чел.")

class Bus(Transport):
    def __init__(self, speed, capacity, route_number):
        super().__init__(speed, capacity)
        self.__route_number = route_number

    def info(self):
        # Переопределяем метод
        print(f"Автобус №{self.__route_number}: скорость {self.__speed} км/ч, вместимость {self.__capacity} чел.")
    

def main():
    t = Transport(120, 50)
    b = Bus(80, 40, "294")
    
    t.info()
    
    b.info()

if __name__ == "__main__":
    main()
    


