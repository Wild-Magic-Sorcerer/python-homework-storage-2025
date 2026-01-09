def main():
    def analyze_string(s):
        # 1. Убираем лишние пробелы по краям
        s = s.strip()
        
        # 2. Считаем слова (split() без аргументов делит по любому количеству пробелов)
        words_list = s.split()
        
        stats = {
            "words": len(words_list),
            "letters": 0,
            "digits": 0,
            "spaces": 0,
            "punctuation": 0
        }
        
        # 3. Проходим по каждому символу исходной строки
        for char in s:
            if char.isalpha():      # Проверка на букву
                stats["letters"] += 1
            elif char.isdigit():    # Проверка на цифру
                stats["digits"] += 1
            elif char.isspace():    # Проверка на пробел
                stats["spaces"] += 1
            elif not char.isalnum(): # Если не буква и не цифра (и не пробел, т.к. проверили выше)
                stats["punctuation"] += 1
                
        return stats
    
    # Проверка
    input_text = input("Введите строку для анализа: ")
    result = analyze_string(input_text)
    
    print("\nРезультат анализа:")
    print(f"Слов: {result['words']}")
    print(f"Букв: {result['letters']}")
    print(f"Цифр: {result['digits']}")
    print(f"Пробелов: {result['spaces']}")
    
    print(f"Знаков препинания: {result['punctuation']}")
if __name__ == "__main__":
    main()

