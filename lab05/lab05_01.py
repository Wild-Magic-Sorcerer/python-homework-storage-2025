# Создайте файл "numbers.txt" с 10 произвольными числами (каждое на новой строке)
# Напишите программу, которая читает файл, находит и выводит максимальное, минимальное и среднее из файла.

with open('numbers.txt', 'w') as file:
    file.write('1\n')
    file.write('1\n')
    file.write('1\n')
    file.write('1\n')
    file.write('1\n')
    file.write('1\n')
    file.write('1\n')
    file.write('1\n')
    file.write('0\n')
    file.write('2\n')
    file.close()
file_in_list = []
with open('numbers.txt', 'r') as file:
    for i in range(10):
        lines_from_file = int(file.readline().replace('\n', ''))
        file_in_list.append(lines_from_file)
    print('Максимальное число в файле:', max(file_in_list))
    print('Минимальное число в файле:', min(file_in_list))
    print('среднее число в файле:', sum(file_in_list)/10)
    file.close()
