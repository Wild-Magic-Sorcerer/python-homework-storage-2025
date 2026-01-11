NUMBERS = [1, 1, 4, 8, 8, 5, 7, 9, 6, 11, 18, 18]


def count_occurrences(data):
    counts = {}

    for num in data:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

result_counts = count_occurrences(NUMBERS)

print("Результаты подсчета:")
for number, count in result_counts.items():

    print(f"{number} — {count}")
    
