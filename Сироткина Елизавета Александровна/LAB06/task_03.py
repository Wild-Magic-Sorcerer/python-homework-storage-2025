#!/usr/bin/env python3

class Person:
    def __init__(self, name: str, profession: str) -> None:
        self.name = name
        self.profession = profession
    
    def introduce(self) -> None:
        print(f"{self.name}, профессия: {self.profession}")


class Employee(Person):
    def __init__(self, name: str, profession: str, position: str) -> None:
        super().__init__(name, profession)
        self.position = position
    
    def introduce(self) -> None:
        super().introduce()
        print(f"  Должность: {self.position}")


class Manager(Employee):
    def __init__(
        self, name: str, profession: str, position: str, department: str
    ) -> None:
        super().__init__(name, profession, position)
        self.department = department
    
    def introduce(self) -> None:
        super().introduce()
        print(f"  Отдел: {self.department}")
    
    def hold_meeting(self) -> None:
        print(f"{self.name} проводит совещание отдела '{self.department}'")


def main() -> None:
    people_list = [
        Person(name="Иван", profession="инженер"),
        Employee(name="Мария", profession="программист", position="Senior Developer"),
        Manager(
            name="Алексей",
            profession="менеджер",
            position="Team Lead",
            department="Разработка",
        ),
    ]
    
    for person in people_list:
        person.introduce()
        print()


if __name__ == "__main__":
    main()
