class Person:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession

    def introduce(self):
        print(f"Привет! Я {self.name}, моя профессия — {self.profession}.")

class Employee(Person):
    def __init__(self, name, profession, position):
        super().__init__(name, profession)
        self.position = position

    def introduce(self):
        # Используем super(), чтобы не дублировать код
        super().introduce()
        print(f"На работе я занимаю должность: {self.position}.")

class Manager(Employee):
    def hold_meeting(self):
        print(f"Менеджер {self.name} собирает совещание!")

# Демонстрация
p = Person("Анна", "Дизайнер")
e = Employee("Игорь", "Программист", "Middle Developer")
m = Manager("Елена", "Управленец", "Project Manager")

print("--- Полиморфизм и цепочка наследования ---")
# Одинаковый вызов для разных классов
people = [p, e, m]
for person in people:
    person.introduce()
    print("-" * 10)

m.hold_meeting()