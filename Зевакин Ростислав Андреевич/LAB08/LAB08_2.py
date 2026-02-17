import re


def main():
    print("Введите строку с датами в формате ДД.ММ.ГГГГ:")
    user_input = input()

    pattern = r'\b(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})\b'

    result = re.sub(pattern, 'DD.MM.YYYY', user_input)

    print("\nРезультат замены:")
    print(result)


if __name__ == "__main__":
    main()