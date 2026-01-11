import random
original_list = random.sample(range(-20, 21), 20)
filtered_list = list(filter(lambda x: x > -5 and x % 2 == 0, original_list))

print(f"Исходный список: {original_list}")

print(f"Отфильтрованный список ( > -5 и чётные): {filtered_list}")
