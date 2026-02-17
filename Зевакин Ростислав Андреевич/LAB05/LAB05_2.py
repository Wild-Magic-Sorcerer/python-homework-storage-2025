filename = "text_file.txt"

user_string = input("Введите строку для добавления в файл: ")

with open(filename, "a", encoding="utf-8") as file:
    file.write(user_string + "")

print(f"Строка добавлена в файл '{filename}'")

print(f"Содержимое файла '{filename}':")

with open(filename, "r", encoding="utf-8") as file:
    lines = file.readlines()

    if not lines:
        print("Файл пуст")
    else:
        for i, line in enumerate(lines, 1):
            print(f"{i}. {line.strip()}")