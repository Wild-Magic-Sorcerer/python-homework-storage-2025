class Person:
    def __init__(self, name, profession):
        self.__name = name
        self.__profession = profession
    def introduce(self):
        print(f"меня зовут {self.__name}, я {self.__profession}")

class Employee(Person):
    def __init__(self, name, profession, position):
        super().__init__(name, profession)
        self.__position = position
    def introduce(self):
        super().introduce()
        print(f"моя должность {self.__position}")

class Manager(Employee):
    def __init__(self, name, profession, position, department):
        super().__init__(name, profession, position)
        self.__department = department
    def hold_meeting(self):
        print(f"мэнеджер {self.__name} проводит совещание  отделе {self.__department}")
        
if __name__ == "__main__":
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


