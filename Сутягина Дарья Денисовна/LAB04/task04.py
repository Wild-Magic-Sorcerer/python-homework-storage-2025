import random

if __name__ == "__main__":
    numbers = [random.randint(-20, 20) for _ in range(15)]
    filtered = list(
        filter(lambda x: x > -5 and x % 2 == 0, numbers)
    )

    print("Исходный список:", numbers)
    print("Отфильтрованный список:", filtered)