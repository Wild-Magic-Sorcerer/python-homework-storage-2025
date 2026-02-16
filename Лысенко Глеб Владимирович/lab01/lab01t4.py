numbers = [1, 2, 3, 3, 1, 6, 5, 3, 7, 1]

count_dict = {}
for number in numbers:
    count_dict[number] = count_dict.get(number, 0) + 1

for number, count in count_dict.items():
    print(f"{number} - {count}")
