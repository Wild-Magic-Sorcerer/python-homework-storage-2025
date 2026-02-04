# Создайте три класса:
# Person — с методом introduce() (выводит имя и профессию);
# Employee, наследующий Person, с переопределением метода introduce() и добавлением поля должности на работе;
# Manager, наследующий Employee, с собственным методом hold_meeting().
# Создайте несколько объектов и продемонстрируйте:
#     Работу цепочки наследования;
#     Вызов родительских методов через super();
#     Полиморфизм: одинаковый вызов метода introduce() для разных классов.

class Person:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession

    def introduce(self):
        return f"{self.name} по профессии: {self.profession}"

class Employee(Person):
    def __init__(self, name, profession, job_title):
        super().__init__(name, profession)
        self.job_title = job_title

    def introduce(self):
        return f"{super().introduce()}, занимает должность: {self.job_title}"

class Manager(Employee):
    def hold_meeting(self):
        return self

Anna = Manager("Anna", "Electrik", "Svarchik")
print(Anna.hold_meeting())
Anna = Employee("Anna", "Electrik", "Svarchik")
print(Anna.introduce())
Anna = Person("Anna", "Electrik")
print(Anna.introduce())

Tom = Person("Tom", "doctor")
print(Tom.introduce())
Tom = Employee("Tom", "doctor", "main doctor")
print(Tom.introduce())
