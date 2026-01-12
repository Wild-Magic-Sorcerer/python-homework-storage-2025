def check_palindrome():
    text = input("введите строку ").strip()

    clean_text = ''.join(text.split())

    left = 0
    right = len(clean_text) - 1

    while left < right:
        if clean_text[left].lower() != clean_text[right].lower():
            print(f"cтрока не является палиндромом,\n несовпадающие символы : позиция {left}: '{clean_text[left]}' и позиция {right}: '{clean_text[right]}'")
            return
        left += 1
        right -= 1

    print("cтрока является палиндромом")

if __name__ == "__main__":
    check_palindrome()

