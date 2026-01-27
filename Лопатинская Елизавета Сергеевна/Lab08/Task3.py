import re

def split_text(text):
    pattern = r"[.,!?;:\-\s]+"
    words = re.split(pattern, text)
    words = [word for word in words if word]
    return words

def main():
    print("--- Программа разделения текста на слова ---")
    user_input = input("Введите предложение со знаками препинания: ")
    if user_input.strip():
        result = split_text(user_input)

        # Вывод результатов
        print("\nСписок слов:")
        print(result)
        print(f"Всего слов: {len(result)}")
    else:
        print("\nОшибка: Строка не должна быть пустой.")

if __name__ == "__main__":
    main()
    
