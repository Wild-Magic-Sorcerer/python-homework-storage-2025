numbers = []

with open("numbers.txt", "r", encoding="utf-8") as file:
    for line in file:
        try:
            numbers.append(float(line.strip()))
        except ValueError:
            pass

if numbers:
    maxV = max(numbers)
    minV = min(numbers)
    avg = sum(numbers) / len(numbers)

    print("Максимальное значение:", maxV)
    print("Минимальное значение:", minV)
    print("Среднее значение:", avg)
else:
    print("Файл не содержит чисел")

