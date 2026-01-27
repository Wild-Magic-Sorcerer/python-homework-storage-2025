def main():
    file_name = "user_data.txt"
    
    # Запрашиваем строку
    new_line = input("Введите строку для добавления в файл: ")
    
    # Добавляем в конец (режим 'a')
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(new_line + "\n")
    
    # Читаем и выводим всё содержимое
    print("\nСодержимое файла:")
    with open(file_name, "r", encoding="utf-8") as f:
    
        print(f.read())
        
if __name__ == "__main__":
    main()

