import re

text = input("Введите строку: ")

words = re.split(r"[ ,.!?\-]+", text)

words = [word for word in words if word]

print("Список слов:")
print(words)
