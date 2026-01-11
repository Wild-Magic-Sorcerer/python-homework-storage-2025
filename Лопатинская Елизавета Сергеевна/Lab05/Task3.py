def copy_and_replace(source_file, target_file):
    try:
        with open(source_file, 'r', encoding='utf-8') as src:
            content = src.read()
        updated_content = content.replace("cat", "dog")
        with open(target_file, 'w', encoding='utf-8') as dst:
            dst.write(updated_content)
        print(
            f"Копирование завершено. Содержимое '{source_file}' перенесено в '{target_file}' с заменой 'cat' на 'dog'.")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{source_file}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


copy_and_replace("source.txt", "destination.txt")
