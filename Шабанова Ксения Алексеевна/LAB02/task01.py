text = input("Введите строку для проверки: ")
# Очистим строку от пробелов и приведем к строчным буквам 
clean_text = text.replace(" ", "").lower()

is_palindrome = True
n = len(clean_text)

for i in range(n // 2):
    # Сравниваем символ с начала и соответствующий ему с конца
    if clean_text[i] != clean_text[n - 1 - i]:
        print(f"Это не палиндром!")
        print(f"Несовпадение: индекс {i} (символ '{clean_text[i]}') и "
              f"индекс {n - 1 - i} (символ '{clean_text[n - 1 - i]}')")
        is_palindrome = False
        break

if is_palindrome:
    print("Ура! Это палиндром.")