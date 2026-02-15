import random
numbers = random.sample(range(-20, 21), 20)
filtered_numbers = list(filter(lambda x : x>-5 and x%2 ==0, numbers))
print(filtered_numbers)
