#1.Модуль для работы с отдельными событиями расписания
from datetime import datetime, timedelta

class Event: #Класс, описывающий учебное событие
    def __init__(self, date_str, time_str, subject, location, duration_min=90):
        self.start_time = datetime.strptime(f"{date_str} {time_str}", "%d.%m.%Y %H:%M")
        self.subject = subject
        self.location = location
        self.duration = timedelta(minutes=duration_min)
        self.end_time = self.start_time + self.duration

    def __str__(self):
        return f"[{self.start_time.strftime('%H:%M')}-{self.end_time.strftime('%H:%M')}] {self.subject} ({self.location})"

#2."Модуль для управления рядом событий
from .event import Event

class Schedule:
    #Класс для хранения и обработки расписания
    def __init__(self):
        self.__events = []  # Инкапсуляция: список событий скрыт

    def add_event(self, event: Event):
        #Добавляет событие, если нет конфликтов
        if self.check_conflict(event):
            print(f"Ошибка: Конфликт расписания для '{event.subject}'")
            return False
        self.__events.append(event)
        self.__events.sort(key=lambda x: x.start_time)
        return True

    def remove_event(self, subject):
        #Удаляет событие по названию предмета
        self.__events = [e for e in self.__events if e.subject != subject]

    def check_conflict(self, new_event: Event):
        #Проверяет наложение временных интервалов
        for e in self.__events:
            if (new_event.start_time < e.end_time and new_event.end_time > e.start_time):
                return True
        return False

    def get_day_schedule(self, date_str):
        #Возвращает список событий на конкретную дату
        target_date = datetime.strptime(date_str, "%d.%m.%Y").date()
        return [e for e in self.__events if e.start_time.date() == target_date]

    def find_free_slots(self, date_str, working_hours=(9, 18)):
        #Поиск свободного времени между занятиями
        day_events = self.get_day_schedule(date_str)
        print(f"Свободные окна на {date_str} (в рамках {working_hours[0]}:00-{working_hours[1]}:00):")

#3.Модуль для работы с данными преподавателей
class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person): #Класс преподавателя, связанный с событиями
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department
        self.assigned_events = []

    def link_event(self, event):
        #Привязывает преподавателя к событию
        self.assigned_events.append(event)

    def get_my_schedule(self):
        #Выводит личное расписание преподавателя
        print(f"Расписание преподавателя {self.name}:")
        for e in self.assigned_events:
            print(f"- {e}")


import argparse
from .event import Event
from .schedule import Schedule
from .teacher import Teacher


def main():
    my_schedule = Schedule()
    teacher = Teacher("Иванов И.И.", "Кафедра ИТ")

    # Демонстрация работы
    e1 = Event("10.10.2025", "09:00", "Программирование", "Ауд. 101")
    e2 = Event("10.10.2025", "10:40", "Математика", "Ауд. 202")

    my_schedule.add_event(e1)
    my_schedule.add_event(e2)
    teacher.link_event(e1)

    print("--- Текущее расписание на 10.10.2025 ---")
    for ev in my_schedule.get_day_schedule("10.10.2025"):
        print(ev)

    teacher.get_my_schedule()


if __name__ == "__main__":
    main()