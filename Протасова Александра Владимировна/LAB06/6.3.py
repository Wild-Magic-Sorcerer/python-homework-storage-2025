class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"Я {self.name}")
class Employee(Person):
    def __init__(self, name, job_title):
        super().__init__(name)
        self.job_title = job_title
    def introduce(self):
        super().introduce()
        print(f"Моя должность: {self.job_title}")
class Manager(Employee):
    def hold_meeting(self):
        print(f"{self.name} проводит встречу")
if __name__ == "__main__":
    person = Person("Саша")
    employee = Employee("Алиса", "разработчик")
    manager = Manager("Маша", "руководитель")
    print("Все объекты созданы\n")
    people = [person, employee, manager]
    for p in people:
        p.introduce()
        print()
    manager.hold_meeting()
