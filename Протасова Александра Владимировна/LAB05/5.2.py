if __name__ == "__main__":
    text = input("Введите текст: ")

    file = open("text_file.txt", "a")
    file.write(text + "\n")
    file.close()

    print("Текст добавлен в файл!")
    print("\nВ файле сейчас:")
    file = open("text_file.txt", "r")
    content = file.read()
    file.close()

    print(content)
