def append_text(filename, text):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text + "\n")


def print_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line.rstrip())


def main():
    filename = "text.txt"
    user_text = input("Введите строку: ")

    append_text(filename, user_text)

    print("\nСодержимое файла:")
    print_file(filename)


if __name__ == "__main__"::
    main()

