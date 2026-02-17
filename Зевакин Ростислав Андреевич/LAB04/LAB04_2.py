fruits = ["apple", "banana", "cherry"]

lengths = list(map(lambda x: len(x), fruits))

print("Исходный список:", fruits)
print("Длины строк:", lengths)

print("Подробно:")
for fruit, length in zip(fruits, lengths):
    print(f"  '{fruit}' -> {length} символов")