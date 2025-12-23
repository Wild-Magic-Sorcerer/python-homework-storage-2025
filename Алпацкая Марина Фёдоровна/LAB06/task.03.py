class Person:
    def __init__(self,name ,profession):
        self._name = name
        self._profession = profession

    def introduce(self):
        print(f'Имя: {self._name}\nПрофессия: {self._profession}')

class Employee(Person):
    def __init__(self,name ,profession, post):
        super().__init__(name ,profession)
        self._post =  post

    def introduce(self):
        print(f'Имя: {self._name}\nПрофессия: {self._profession}\nДолжность: {self._post}')

class Manager(Employee):
    def __init__(self,name ,profession, post, time):
        super().__init__(name, profession, post)
        self._time = time

    def hold_meeting(self):
        print(f'Проведём встречу через {self._time} часов')


if __name__ == '__main__':
    name_person = input(f'Введите имя: ')
    profession_person = input(f'Введите профессию: ')
    post_person = input(f'Введите должность: ')
    time_person = input(f'Введите время: ')

    person1 = Person(name_person,profession_person)
    person1.introduce()

    person2 = Employee(name_person,profession_person,post_person)
    person2.introduce()

    person3 = Manager(name_person,profession_person,post_person,time_person)
    person3.introduce()
    person3.hold_meeting()



