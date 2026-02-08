is_even = lambda x: x % 2 == 0

if __name__ == "__main__":
    for number in range(1, 11):
        result = is_even(number)
        print(f"Число {number}: {'чётное' if result else 'нечётное'} ({result})")
