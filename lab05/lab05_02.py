# Реализуйте программу, которая запрашивает у пользователя строку и добавляет её в существующий текстовый файл
# После добавления выведите все строки этого файла на экран.

print('Пожалуйста введите строчку своего текста')
line_from_user = str(input())
with open('lab05_02_file.txt', 'a') as file:
    file.write(line_from_user + '\n')
    file.close()
with open('lab05_02_file.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            line = file.readline().replace('\n', '')
            continue
        print(line)
    file.close()
