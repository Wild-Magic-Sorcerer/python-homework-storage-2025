class Person:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession

    def introduce(self):
        print(f"Меня зовут {self.name}. Моя профессия - {self.profession}.")

class Employee(Person):
    def __init__(self, name, profession, position):
        super().__init__(name, profession)
        self.position = position

    def introduce(self):
        super().introduce()
        print(f"Моя должность на работе - {self.position}.")

class Manager(Employee):
    def __init__(self, name, profession, position):
        super().__init__(name, profession, position)

    def hold_meeting(self):
        print(f"{self.name} проводит совещание.")


person = Person("Иван", "программист")
employee = Employee("Анна", "инженер", "старший инженер")
manager = Manager("Олег", "менеджер", "руководитель отдела")

person.introduce()
employee.introduce()
manager.introduce()

manager.hold_meeting()
