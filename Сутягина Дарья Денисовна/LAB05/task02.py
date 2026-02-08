filename = "text.txt"

user_text = input("Введите строку: ")

with open(filename, "a", encoding="utf-8") as file:
    file.write(user_text + "\n")

print("\nСодержимое файла:")
with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())
