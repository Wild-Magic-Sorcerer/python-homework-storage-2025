if __name__ == '__main__':
    users_str = input("Введите строку")
    with open("file_for_lab05.2.txt", "a") as file:
        file.write(f"{users_str}\n")
    with open("file_for_lab05.2.txt", "r") as file:
        lines = file.read()
        print(f"Содержимое файла:\n {lines}")


