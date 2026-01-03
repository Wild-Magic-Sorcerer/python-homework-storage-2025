text = input("Введите текст: ")
vowels = "аеёиоуыэюяaeiouy"
result = ""

for char in text:
    if char.lower() in vowels:
        result += char.upper()
    elif char.isalpha(): # Если буква, но не гласная — значит согласная
        result += char.lower()
    else:
        result += char # Цифры и знаки оставляем как есть

print("Результат:", result)