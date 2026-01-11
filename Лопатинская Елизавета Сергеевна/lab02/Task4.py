from datetime import datetime

def print_date_details(date_string):
    dt_obj = datetime.strptime(date_string, "%d.%m.%Y %H:%M:%S")

    print(f"\nДетальная информация:")
    print(f"  День: {dt_obj.day}")
    print(f"  Месяц: {dt_obj.month}")
    print(f"  Год: {dt_obj.year}")
    print(f"  Часы: {dt_obj.hour}")
    print(f"  Минуты: {dt_obj.minute}")
    print(f"  Секунды: {dt_obj.second}")

def main():
    print("--- Программа разбора даты и времени ---")
    user_input = input("Введите дату и время (ДД.ММ.ГГГГ ЧЧ:ММ:СС): ")
    try:
        print_date_details(user_input)
    except ValueError:
        print("\nОшибка: Неверный формат даты.")
        print("Пожалуйста, используйте шаблон: ДД.ММ.ГГГГ ЧЧ:ММ:СС (например, 31.12.2025 23:52:52)")

if __name__ == "__main__":
    main()
