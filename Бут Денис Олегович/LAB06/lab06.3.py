class Person:
    def __init__(self,name,profession):
        self.name = name
        self.profession = profession
    def introduce (self):
        return f"Имя:{self.name}, профеcсия:{self.profession}"

class Employee(Person):
    def __init__(self,name,profession,post):
        super().__init__(name,profession)
        self.post = post

    def introduce(self):
        return f"На работу был(а) нанят: имя:{self.name}, профеcсия:{self.profession}, должность:{self.post}"

class Manager(Employee):
    def __init__(self,name,post):
        super().__init__(name,"doctor",post)

    def hold_meeting (self):
        return f"На встречу пришёл:{self.name}, занимающий должность:{self.post}"

if __name__ == "__main__":
    some_people = [Person("Robert","dispather"),
                   Employee("Sandy","Croupier","Rookie"),
                   ]
    some_person = Manager("Ted","Head")

    for person in some_people:
        print(person.introduce())
    print(some_person.hold_meeting())


