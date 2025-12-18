#!/usr/bin/env python3
"""Цепочка наследования Person -> Employee -> Manager."""


class Person:
    """Человек."""
    
    def __init__(self, name: str, profession: str) -> None:
        self.name = name
        self.profession = profession
    
    def introduce(self) -> None:
        print(f"{self.name}, {self.profession}")


class Employee(Person):
    """Сотрудник."""
    
    def __init__(self, name: str, profession: str, position: str) -> None:
        super().__init__(name, profession)
        self.position = position
    
    def introduce(self) -> None:
        super().introduce()
        print(f"  Должность: {self.position}")


class Manager(Employee):
    """Менеджер отдела."""
    
    def __init__(self, name: str, profession: str, position: str, department: str) -> None:
        super().__init__(name, profession, position)
        self.department = department
    
    def introduce(self) -> None:
        super().introduce()
        print(f"  Отдел: {self.department}")
    
    def hold_meeting(self) -> None:
        print(f"{self.name} проводит совещание отдела '{self.department}'")


def main() -> None:
    people = [
        Person("Иван", "инженер"),
        Employee("Мария", "программист", "Senior Developer"),
        Manager("Алексей", "менеджер", "Team Lead", "Разработка"),
    ]
    
    for p in people:
        p.introduce()
        print()


if __name__ == "__main__":
    main()
