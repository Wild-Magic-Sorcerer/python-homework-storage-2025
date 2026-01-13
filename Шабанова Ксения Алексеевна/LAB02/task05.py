import re

def get_words(text):
    # 1. Переводим в нижний регистр
    text = text.lower()
    words = re.findall(r'\w+', text)
    # 2. Превращаем список во множество для сравнения
    return set(words)

def main():
    # Ввод данных
    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")
    
    # Обработка
    set1 = get_words(str1)
    set2 = get_words(str2)
    
    # Проверка и вывод
    if set1 == set2:
        print("\nРезультат: Строки равны")
    else:
        only_in_1 = set1 - set2
        only_in_2 = set2 - set1
        
        print("\nРезультат: Строки не равны")
        if only_in_1:
            print(f"Есть в первой, но нет во второй: {', '.join(only_in_1)}")
        if only_in_2:
    
            print(f"Есть во второй, но нет в первой: {', '.join(only_in_2)}")

if __name__ == "__main__":
    main()


