from collections import Counter
numbers = [1, 2, 3, 3, 1, 6, 5, 3, 7, 1]
count_dict = Counter(numbers)
for number, count in count_dict.items():
    print(f"{number} — {count}")