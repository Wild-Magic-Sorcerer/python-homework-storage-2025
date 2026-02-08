if __name__ == '__main__':
    s = input("Введите строку: ")

    palindrome = True

    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            print("Строка не является палиндромом")
            print(f"Несоответствие начинается с {i} символа")
            print(f"Слева: '{s[i]}', справа: '{s[len(s) - 1 - i]}'")
            palindrome = False
            break

    if palindrome:
        print("Строка является палиндромом")