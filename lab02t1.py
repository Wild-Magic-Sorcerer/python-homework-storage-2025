def is_palindrome(s):
    cleaned_s = ''.join(s.split()).lower()
    left = 0
    right = len(cleaned_s) - 1

    while left < right:
        if cleaned_s[left] != cleaned_s[right]:
            return False, left, cleaned_s[left], right, cleaned_s[right]
        left += 1
        right -= 1
    return True, None, None, None, None

user_input = input("Введите строку: ")

is_pal, left_index, left_char, right_index, right_char = is_palindrome(user_input)

if is_pal:
    print("Строка является палиндромом.")
else:
    print(f"Строка не является палиндромом. Отличие на символах: "
          f"индекс {left_index} ('{left_char}') и индекс {right_index} ('{right_char}').")