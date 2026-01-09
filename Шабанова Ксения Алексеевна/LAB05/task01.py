def main():
    # Создаем файл с числами
    numbers = [12, 45, 7, 23, 56, 89, 34, 1, 90, 15]
    with open("numbers.txt", "w") as f:
        for n in numbers:
            f.write(f"{n}\n")
    
    # Читаем файл и считаем статистику
    with open("numbers.txt", "r") as f:
        # Читаем строки, убираем пробелы и превращаем в int
        data = [int(line.strip()) for line in f]
    
    if data:
        print(f"Максимум: {max(data)}")
        print(f"Минимум: {min(data)}")
    
        print(f"Среднее: {sum(data) / len(data)}")
        
if __name__ == "__main__":
    main()

