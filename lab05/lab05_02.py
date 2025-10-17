# Реализуйте программу, которая запрашивает у пользователя строку и добавляет её в существующий текстовый файл
# После добавления выведите все строки этого файла на экран.

print('Пожалуйста введите строчку своего текста')
line_from_user = str(input())
with open('lab05_02_file.txt', 'a') as file:
    file.write(f'{line_from_user}\n')
with open('lab05_02_file.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            line = file.readline().replace('\n', '')
            continue
        print(line)
