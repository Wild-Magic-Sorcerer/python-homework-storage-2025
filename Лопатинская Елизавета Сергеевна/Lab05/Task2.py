def append_to_file(file_name, text):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(text + "\n")
    print(f"\n--- Запись в '{file_name}' завершена ---")

def read_file_content(file_name):
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

def main():
    target_file = "numbers.txt"
    user_text = input("Введите текст, который хотите добавить в файл: ")

    append_to_file(target_file, user_text)
    read_file_content(target_file)

if __name__ == "__main__":
    main()
    
