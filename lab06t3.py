class Person:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession

    def introduce(self):
        print(f"Меня зовут {self.name}, я {self.profession}.")


class Employee(Person):
    def __init__(self, name, profession, position):
        super().__init__(name, profession)
        self.position = position

    def introduce(self):
        super().introduce()
        print(f"Я работаю на должности: {self.position}.")


class Manager(Employee):
    def __init__(self, name, profession, position):
        super().__init__(name, profession, position)

    def hold_meeting(self):
        print(f"{self.name} проводит собрание.")


person1 = Person("Иван", "студент")
person1.introduce()

print()

employee1 = Employee("Анна", "инженер", "разработчик")
employee1.introduce()

print()

manager1 = Manager("Сергей", "менеджер", "руководитель проекта")
manager1.introduce()
manager1.hold_meeting()