if __name__ == "__main__":
    text = input("Введите текст: ")

    with open("text_file.txt", "a") as file:
        file.write(text + "\n")

    print("Текст добавлен в файл!")
    print("\nВ файле сейчас:")

    with open("text_file.txt", "r") as file:
        content = file.read()

    print(content)
