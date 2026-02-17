class Person:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession

    def introduce(self):
        return f"Я {self.name}. Я работаю {self.profession}."


class Employee(Person):
    def __init__(self, name, profession, position):
        super().__init__(name, profession)
        self.position = position

    def introduce(self):
        intro = super().introduce()
        return f"{intro} Моя должность: {self.position}."


class Manager(Employee):
    def __init__(self, name, profession, position, department):
        super().__init__(name, profession, position)
        self.department = department

    def introduce(self):
        intro = super().introduce()
        return f"{intro} Я руковожу отделом: {self.department}."

    def hold_meeting(self, topic):
        return f"Провожу собрание по теме: '{topic}' для отдела {self.department}"


def demonstrate_super():
    print("Работа super()")

    person = Person("Ольга", "учителем")
    employee = Employee("Андрей", "врачом", "эндокринолог")
    manager = Manager("Антон", "менеджером", "руководитель", "разработка игр")

    print("\n1. Вызов методов:")

    print("\nperson.introduce():" f" '{person.introduce()}'")

    print("\nemployee.introduce:" f" '{employee.introduce()}'")

    print("\nmanager.introduce():" f" '{manager.introduce()}'")

    print("3. Полиморфизм")

    people_list = [person, employee, manager]

    print("\nСписок содержит объекты разных типов:")
    for i, obj in enumerate(people_list, 1):
        print(f"  {i}. {type(obj).__name__}: {obj.name}")

    print("\nВызов introduce() для каждого объекта:")

    for obj in people_list:
        result = obj.introduce()
        print(f"{type(obj).__name__}.introduce(): {result}")

    print("\n4. Проверка isinstance()")

    test_cases = [
        ("person", person),
        ("employee", employee),
        ("manager", manager)
    ]

    for name, obj in test_cases:
        print(f"\n{name} ({type(obj).__name__}):")

        is_person = isinstance(obj, Person)
        is_employee = isinstance(obj, Employee)
        is_manager = isinstance(obj, Manager)

        print(f" isinstance(obj, Person) = {is_person}")
        print(f" isinstance(obj, Employee) = {is_employee}")
        print(f" isinstance(obj, Manager) = {is_manager}")

        if is_manager:
            print(f" может проводить собрания")
            print(f"  {obj.hold_meeting('Технические вопросы')}")
        elif is_employee:
            print(f" имеет должность: {obj.position}")
      
if __name__ == "__main__":
    demonstrate_super()
