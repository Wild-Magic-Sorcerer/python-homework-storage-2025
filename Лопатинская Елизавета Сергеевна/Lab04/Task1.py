is_even = lambda x: x % 2 == 0

print(f"{'Число':<10} | {'Чётное?':<10}")
print("-" * 25)

for i in range(1, 11):
    result = is_even(i)
    print(f"{i:<10} | {result:<10}")