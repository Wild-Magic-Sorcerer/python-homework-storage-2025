def filter_unique_lines(input_file, output_file):
    unique_lines = set()
    duplicates = []

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                clean_line = line.strip()
                if not clean_line:
                    continue

                if clean_line in unique_lines:
                    duplicates.append(clean_line)
                else:
                    unique_lines.add(clean_line)


        with open(output_file, 'w', encoding='utf-8') as f:
            for line in unique_lines:
                f.write(line + '\n')

        print(f"Обработка завершена. Уникальные строки сохранены в '{output_file}'.")
        if duplicates:
            print("\nНайденные неуникальные строки (дубликаты):")
            for dup in set(duplicates):
                print(f"- {dup}")
        else:
            print("\nПовторяющихся строк не обнаружено.")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден.")


filter_unique_lines("data.txt", "unique_data.txt")
