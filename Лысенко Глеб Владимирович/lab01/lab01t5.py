import random

    numbers = [random.randint(-10, 10) for _ in range(15)]

    multiples_of_three = [num for num in numbers if num % 3 == 0]

print(f"Исходный список: {numbers}")
print(f"Только кратные 3: {multiples_of_three}")

