def main():
    input_file = "data.txt"
    unique_file = "unique.txt"
    
    # Для примера создадим файл с повторами
    with open(input_file, "w") as f:
        f.write("apple\nbanana\napple\ncherry\nbanana\n")
    
    all_lines = []
    unique_lines = []
    non_unique = []
    
    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            if line in unique_lines:
                non_unique.append(line)
            else:
                unique_lines.append(line)
    
    # Сохраняем только уникальные
    with open(unique_file, "w") as f:
        for line in unique_lines:
            f.write(line + "\n")
    
    
    print(f"Неуникальные строки: {', '.join(non_unique)}")

if __name__ == "__main__":
    main()


