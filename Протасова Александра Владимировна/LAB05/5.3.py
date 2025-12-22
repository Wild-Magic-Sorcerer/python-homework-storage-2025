if __name__ == "__main__":
    source_filename = "source.txt"
    destination_filename = "destination.txt"

    try:
        with open(source_filename, "r") as source_file:
            original_text = source_file.read()

        new_text = original_text.replace("cat", "dog")

        with open(destination_filename, "w") as dest_file:
            dest_file.write(new_text)

        print(f"Файл '{source_filename}' скопирован в '{destination_filename}'")
        print("Все слова 'cat' заменены на 'dog'")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{source_filename}' не найден")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
