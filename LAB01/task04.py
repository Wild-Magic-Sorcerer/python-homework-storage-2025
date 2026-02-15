NUMBERS = [3, 7, 2, 3, 5, 7, 7, 2, 1, 8, 3, 5, 5, 5]

count_dict = {}
for num in NUMBERS:
    count_dict[num] = count_dict.get(num, 0) + 1

for num in sorted(count_dict):
    print(f"{num} — {count_dict[num]}")
