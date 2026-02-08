source = "source.txt"
target = "target.txt"

with open(source, "r", encoding="utf-8") as src:
    content = src.read()

# 2. Заменяем "cat" на "dog"
content = content.replace("cat", "dog")

# 3. Записываем результат во второй файл
with open(target, "w", encoding="utf-8") as tgt:
    tgt.write(content)

print("Копирование завершено. Все слова 'cat' заменены на 'dog'.")
