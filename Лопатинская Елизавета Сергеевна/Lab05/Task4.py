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
            for line in sorted(unique_lines):  # Сортировка добавлена для порядка
                f.write(line + '\n')
        print(f"Обработка завершена. Уникальные строки сохранены в '{output_file}'.")
        
        if duplicates:
            print("\nНайденные неуникальные строки (дубликаты):")
            for dup in sorted(set(duplicates)):
                print(f"- {dup}")
        else:
            print("\nПовторяющихся строк не обнаружено.")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

def main():
    source = "data.txt"
    destination = "unique_data.txt"
    
    print(f"--- Запуск фильтрации строк в файле {source} ---")
    filter_unique_lines(source, destination)
    print("--- Работа программы завершена ---")

if __name__ == "__main__":
    main()
    
