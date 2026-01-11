import re

def mask_dates(text):
    date_pattern = r"\d{2}\.\d{2}\.\d{4}"
    result = re.sub(date_pattern, "DD.MM.YYYY", text)
    return result

def main():
    print("--- Программа маскирования дат ---")
    user_input = input("Введите текст, содержащий даты (например, 01.01.2024): ")
    
    if user_input.strip():
        output = mask_dates(user_input)
        
        print("\nРезультат обработки:")
        print(output)
    else:
        print("\nОшибка: Введена пустая строка.")

if __name__ == "__main__":
    main()
    
