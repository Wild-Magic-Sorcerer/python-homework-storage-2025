def check_palindrome():
    raw_text = input("Введите строку для проверки: ")
    clean_text = "".join(char.lower() for char in raw_text if char.isalnum())

    if not clean_text:
        print("Строка пуста или не содержит символов для проверки.")
        return

    is_palindrome = True
    length = len(clean_text)

    for i in range(length // 2):
        left_char = clean_text[i]
        right_char = clean_text[length - 1 - i]

        if left_char != right_char:
            is_palindrome = False
            print(f"\nСтрока НЕ является палиндромом.")
            print(f"Несоответствие найдено:")
            print(f"- Слева: индекс {i}, символ '{left_char}'")
            print(f"- Справа: индекс {length - 1 - i}, символ '{right_char}'")
            break

    if is_palindrome:
        print("\nПоздравляем! Это палиндром.")

def main():
    print("--- Программа проверки палиндромов ---")
    check_palindrome()
    print("\nПрограмма завершена.")

if __name__ == "__main__":
    main()



