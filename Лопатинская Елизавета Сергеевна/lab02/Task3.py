def transform_string(text):
    vowels = "аеёиоуыэюяaeiouyАЕЁИОУЫЭЮЯAEIOUY"
    result = ""

    for char in text:
        if char.isalpha():
            if char in vowels:
                result += char.upper()  # Гласную — в заглавную
            else:
                result += char.lower()  # Согласную — в строчную
        else:
            result += char

    return result

user_input = input("Введите строку: ")
final_text = transform_string(user_input)


print(f"Результат: {final_text}")

