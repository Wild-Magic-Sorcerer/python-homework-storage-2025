# Создайте программу, которая построчно читает файл и сохраняет только уникальные строки в новый файл
# В конце программа должна вывести на экран все неуникальные строки

non_unique_variable = []
with open('lab05_04_file.txt', 'r') as file:
    variable = file.readlines()
    for i in range(5):
        if variable.count(variable[i]) > 1:
            non_unique_variable.append(variable[i])
        else: continue
    print('все неуникальные строки:',non_unique_variable)
    file.close()
