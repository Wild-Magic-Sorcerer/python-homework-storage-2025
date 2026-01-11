class Person:
    def __init__(self, name):
        self.name = name
        self.vocation = "Биоинформатик"

    def introduce(self):
        print(f"Привет! Меня зовут {self.name}. Моя профессия: {self.vocation}.")

class Employee(Person):
    def __init__(self, name, position):
        super().__init__(name)
        self.position = position
        self.vocation = "лаборант"

    def introduce(self):
        print(f"Здравствуйте! Я {self.name}, работаю на должности: {self.position}.")

class Manager(Employee):
    def __init__(self, name, position, department):
        super().__init__(name, position)
        self.department = department

    def hold_meeting(self):
        print(f"Менеджер {self.name} собирает совещание отдела {self.department}...")


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

    print(f"\nПроверка атрибутов Manager: Имя={boss.name}, Должность={boss.position}")

if __name__ == "__main__":
    main()
    
