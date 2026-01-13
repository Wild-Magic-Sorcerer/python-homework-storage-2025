class Person:
    def __init__(self, name):
        self.__name = name
        self.__vocation = "Биоинформатик"

    def get_name(self):
        """Метод для получения имени."""
        return self.__name

    def get_vocation(self):
        """Метод для получения профессии."""
        return self.__vocation

    def set_vocation(self, value):
        """Метод для изменения профессии с проверкой."""
        if isinstance(value, str) and value:
            self.__vocation = value

    def introduce(self):
        print(f"Привет! Меня зовут {self.__name}. Моя профессия: {self.__vocation}.")

class Employee(Person):
    def __init__(self, name, position):
        super().__init__(name)
        self.__position = position
        self.set_vocation("лаборант")

    def get_position(self):
        """Метод для получения должности."""
        return self.__position

    def introduce(self):
        print(f"Здравствуйте! Я {self.get_name()}, работаю на должности: {self.__position}.")

class Manager(Employee):
    def __init__(self, name, position, department):
        super().__init__(name, position)
        self.__department = department

    def get_department(self):
        """Метод для получения отдела."""
        return self.__department

    def hold_meeting(self):
        print(f"Менеджер {self.get_name()} собирает совещание отдела {self.__department}...")

def main():
    person = Person("Иван")
    worker = Employee("Анна", "Разработчик")
    boss = Manager("Сергей", "Технический директор", "IT")

    print("--- Проверка полиморфизма ---")
    people = [person, worker, boss]
    for p in people:
        p.introduce()

    print("\n--- Проверка специфичных методов ---")
    boss.hold_meeting()

    print(f"\nПроверка атрибутов Manager:")
    print(f"Имя: {boss.get_name()}")
    print(f"Должность: {boss.get_position()}")
    print(f"Отдел: {boss.get_department()}")
    
    print("\n--- Проверка защиты ---")
    boss.__name = "Хакер" 
    print(f"Результат вызова get_name(): {boss.get_name()} (не изменилось)")

if __name__ == "__main__":
    main()
    

