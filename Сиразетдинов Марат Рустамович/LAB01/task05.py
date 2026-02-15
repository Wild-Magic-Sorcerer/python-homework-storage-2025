import random

numbers = [random.randint(-10, 10) for i in range(20)]
print("Исходный список", numbers)

multiplies_of_3 = [num for num in range(10) if num % 3 == 0]
print(multiplies_of_3)
