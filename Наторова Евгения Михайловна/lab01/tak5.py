import random
if __name__ == "__main__":
    list = [random.randint(-10, 10) for _ in range(15)]

    spisok = [num for num in list if num % 3 == 0]

    print(f"Исходный список: {list},"

          f"Числа, кратные 3: {spisok}")
    
