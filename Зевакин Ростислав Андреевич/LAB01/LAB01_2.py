a, b, c = "Зоология", "Ботаника", "Физкультура"
st_list = []

while True:
    t_input = input("Введите имя студента, его оценки по Зоологии, Ботанике и Физкультуре через пробел (если студентов больше нет введите 'стоп'): ")
    if t_input.lower() == 'стоп':
        break
    marks = t_input.split()

    if len(marks) != 4:
        print("Ошибка: должно быть 3 оценки")
        continue

    name = marks[0]

    if any(name_name.isdigit() for name_name in name):
        print("Ошибка: впишите имя")
        continue
    try:
        mark1 = int(marks[1])
        mark2 = int(marks[2])
        mark3 = int(marks[3])

        numbers = [mark1, mark2, mark3]

        valid_marks = True
        for grade in numbers:
            if grade < 3 or grade > 5:
                print("Ошибка: оценки должны быть от 3 до 5")
                valid_marks = False
                break

        if valid_marks:
            st_list.append([name, mark1, mark2, mark3])
            print("Оценки добавлены")

    except ValueError:
        print("Ошибка: после имени должны быть три числа")
    except IndexError:
        print("Ошибка: недостаточно данных")

print("Оценки студентов:")

for student in st_list:
    name = student[0]
    grades = student[1:]
    print(f"{name}: {a} - {grades[0]}, {b} - {grades[1]}, {c} - {grades[2]}")

all_marks = []
z_marks = []
b_marks = []
f_marks = []

for human in st_list:
    name = human[0]
    marks = human[1:]

    all_marks.extend(marks)
    z_marks.append(marks[0])
    b_marks.append(marks[1])
    f_marks.append(marks[2])


    end_all = sum(all_marks) / len(all_marks)
    end_z = sum(z_marks) / len(z_marks)
    end_b = sum(b_marks) / len(b_marks)
    end_f = sum(f_marks) / len(f_marks)

print(f"Средний балл по всем предметам: {end_all}")
print(f"Срединй балл по зоологии: {end_z}")
print(f"Средний балл по ботанике: {end_b}")
print(f"Средний балл по физкультуре: {end_f}")
