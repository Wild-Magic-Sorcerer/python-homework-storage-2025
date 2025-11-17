def check_palindrome_simple(text):
    original_text = text
    reversed_text = text[::-1]

    if text == reversed_text:
        print(f"Строка '{original_text}' является палиндромом.")
        return True
    else:
        print(f"Строка '{original_text}' НЕ является палиндромом.")

        n = len(text)
        first_diff_index = -1
        for i in range(n):
            if text[i] != reversed_text[i]:
                first_diff_index = i
                break

        if first_diff_index != -1:
            print(f"Расхождение начинается с индекса {first_diff_index}:")
            print(f"  Символ слева: '{text[first_diff_index]}'")
            print(f"  Символ справа (при чтении справа налево): '{reversed_text[first_diff_index]}'")
        else:
            print("Не удалось найти конкретное расхождение.")
        return False
