import re
def split_text(text):
    pattern = r"[.,!?;:\-\s]+"
    words = re.split(pattern, text)
    words = [word for word in words if word]
    return words


# Пример работы
user_input = input("Введите предложение со знаками препинания: ")
result = split_text(user_input)

print("\nСписок слов:")
print(result)
print(f"Всего слов: {len(result)}")