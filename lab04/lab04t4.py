import random
random_list = random.sample(range(-20, 21), 20)
filtered_list = list(filter(lambda x: x > -5 and x % 2 == 0, random_list))

print("Исходный список:", random_list)
print("Отфильтрованный список:", filtered_list)