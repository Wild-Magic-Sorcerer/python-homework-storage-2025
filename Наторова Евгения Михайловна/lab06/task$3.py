class Person:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession
    def introduce(self):
        print(f"меня зовут {self.name}, я {self.profession}")

class Employee(Person):
    def __init__(self, name, profession, position):
        super().__init__(name, profession)
        self.position = position
    def introduce(self):
        super().introduce()
        print(f"моя должность {self.position}")

class Manager(Employee):
    def __init__(self, name, profession, position, department):
        super().__init__(name, profession, position)
        self.department = department
    def hold_meeting(self):
        print(f"мэнеджер {self.name} проводит совещание  отделе {self.department}")

print("первый пункт")
persona5= Person('ася', "бухгалтер")
emp1= Employee("вася","охранник", "начальник охраны")
man1= Manager('Дуся', "менеджер", "руководитель отдела", "инвестиции")

print("второй пункт")
persona5.introduce()
emp1.introduce()
man1.introduce()
man1.hold_meeting()
print("третий пункт")
people = [persona5, emp1, man1]
for person in people:
    person.introduce()
