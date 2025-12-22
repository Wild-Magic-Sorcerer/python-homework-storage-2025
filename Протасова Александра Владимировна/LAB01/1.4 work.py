numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counts = {}
for number in numbers:
    if number in counts:
        counts[number] += 1  # если число уже есть в словаре
    else:
        counts[number] = 1  # если числа нет в словаре
for number, count in counts.items():
    print(f"{number} - {count}")
