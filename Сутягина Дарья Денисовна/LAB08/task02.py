import re

text = input("Введите строку с датой: ")

pattern = r"\b\d{2}\.\d{2}\.\d{4}\b"

result = re.sub(pattern, "DD.MM.YYYY", text)

print("Результат:")
print(result)
