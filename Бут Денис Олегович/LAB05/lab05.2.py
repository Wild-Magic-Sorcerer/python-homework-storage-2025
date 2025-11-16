if __name__ == '__main__':
    users_str = str(input("Введите строку"))
    with open("file_for_lab05.2.txt", "a") as file:
        file.write(f"\n{users_str}")
    with open("file_for_lab05.2.txt", "r") as file:
        lines = file.read()
        print(f"Содержимое файла:\n {lines}")

