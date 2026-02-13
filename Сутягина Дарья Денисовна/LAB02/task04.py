def parse_datetime(text: str):
    parts = text.split()

    if len(parts) != 2:
        raise ValueError("Неверный формат")

    date_part, time_part = parts

    day, month, year = date_part.split(".")
    hour, minute, second = time_part.split(":")

    return day, month, year, hour, minute, second


def main():
    while True:
        user_input = input("Введите дату и время (ДД.ММ.ГГГГ ЧЧ:ММ:СС): ")

        try:
            day, month, year, hour, minute, second = parse_datetime(user_input)

            print(f"День: {day}")
            print(f"Месяц: {month}")
            print(f"Год: {year}")
            print(f"Часы: {hour}")
            print(f"Минуты: {minute}")
            print(f"Секунды: {second}")
            break

        except ValueError:
            print("Ошибка формата. Попробуйте снова.\n")


if __name__ == "__main__":
    main()
