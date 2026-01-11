file_name = "numbers.txt"
new_line = input("Введите текст, который хотите добавить в файл: ")

with open(file_name, "a", encoding="utf-8") as file:
    file.write(new_line + "\n")

print(f"\n--- Запись в '{file_name}' завершена ---")

print("Текущее содержимое файла:")
try:
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
        if content:
            print(content)
        else:
            print("[Файл пуст]")
except FileNotFoundError:

    print(f"Ошибка: Файл '{file_name}' не найден.")
    
