# Реализуйте программу, которая запрашивает у пользователя строку и добавляет её в существующий текстовый файл
# После добавления выведите все строки этого файла на экран.

line_from_user = input('Пожалуйста введите строчку своего текста ')
with open('lab05_02_file.txt', 'a') as file:
    file.write(f'{line_from_user}\n')
with open('lab05_02_file.txt', 'r') as file:
    for line in file.readlines():
        print(line.replace('\n', ''))
