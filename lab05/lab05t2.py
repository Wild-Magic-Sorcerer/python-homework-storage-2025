user_input = input("Введите строку для добавления в файл: ")

with open('example.txt', 'a', encoding='utf-8') as file:
    file.write(user_input + '\n')

with open('example.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

print("Содержимое файла:")
for line in lines:
    print(line.strip())