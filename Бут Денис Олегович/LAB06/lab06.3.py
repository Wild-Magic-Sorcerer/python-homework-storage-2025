class Person:
    def __init__(self, name, profession):
        self._name = name
        self._profession = profession

    def introduce(self):
        return f"Имя:{self._name}, профессия:{self._profession}"


class Employee(Person):
    def __init__(self, name, profession, post):
        super().__init__(name, profession)
        self._post = post
    def introduce(self):
        return f"На работу был(а) нанят: имя:{self._name}, профессия:{self._profession}, должность:{self._post}"


class Manager(Employee):
    def __init__(self, name, post):
        super().__init__(name, "doctor", post)

    def hold_meeting(self):
        return f"На встречу пришёл:{self._name}, занимающий должность:{self._post}"


if __name__ == "__main__":
    some_people = [
        Person("Robert", "dispather"),
        Employee("Sandy", "Croupier", "Rookie"), ]
    some_person = Manager("Ted", "Head")

    printed = [print(person.introduce()) for person in some_people]
    print(some_person.hold_meeting())