# Создайте файл "numbers.txt" с 10 произвольными числами (каждое на новой строке)
# Напишите программу, которая читает файл, находит и выводит максимальное, минимальное и среднее из файла.

a = (45, 79, 87, 0, -1, -15, 0, 98, 2, 13)
with open('numbers.txt', 'w') as file:
    for i in a:
        file.write(f'{i}\n')
file_in_list = []
with open('numbers.txt', 'r') as file:
    for i in a:
        lines_from_file = int(file.readline().replace('\n', ''))
        file_in_list.append(lines_from_file)
    print('Максимальное число в файле:', max(file_in_list))
    print('Минимальное число в файле:', min(file_in_list))
    print('среднее число в файле:', sum(file_in_list)/len(a))
