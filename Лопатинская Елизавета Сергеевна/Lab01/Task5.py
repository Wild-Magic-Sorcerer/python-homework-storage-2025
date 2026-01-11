original_list = list(range(-10, 11))

filtered_list = [num for num in original_list if num % 3 == 0]

print(f"Исходный список: {original_list}")
print(f"Числа, кратные 3: {filtered_list}")