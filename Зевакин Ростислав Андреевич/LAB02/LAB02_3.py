text = input("Введите строку: ")

vowels = "aeiouаеёиоуыэюя"

result = ""

for char in text:
    if char.isalpha():
        small_char = char.lower()
        if small_char in vowels:
            result = result + small_char.upper()
        else:
            result = result + small_char
    else:
        result = result + char

print("Результат:", result)