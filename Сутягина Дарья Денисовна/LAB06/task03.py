class Person:
    def init(self, name, profession):
        self.name = name
        self.profession = profession

    def introduce(self):
        print(f"Меня зовут {self.name}. Моя профессия - {self.profession}.")


class Employee(Person):
    def init(self, name, profession, position):
        super().init(name, profession)
        self.position = position

    def introduce(self):
        super().introduce()
        print(f"Моя должность - {self.position}.")


class Manager(Employee):
    def hold_meeting(self):
        print(f"{self.name} проводит совещание.")


if name == "main":
    person = Person("Иван", "программист")
    employee = Employee("Анна", "инженер", "старший инженер")
    manager = Manager("Олег", "менеджер", "руководитель отдела")

    person.introduce()
    print()

    employee.introduce()
    print()

    manager.introduce()
    manager.hold_meeting()
