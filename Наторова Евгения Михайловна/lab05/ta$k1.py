import random

if __name__ == "__main__":
    with open("numbers.txt", "w") as file:
        for i in range(10):
            file.write(str(random.randint(1, 1000)) + "\n")

    with open("numbers.txt", "r") as file:
        numbers = []
        for line in file:
            if line.strip():
                numbers.append(int(line.strip()))

    if numbers:
        max_num = numbers[0]
        for num in numbers:
            if num > max_num:
                max_num = num

        min_num = numbers[0]
        for num in numbers:
            if num < min_num:
                min_num = num

        total = 0
        count = 0
        for num in numbers:
            total += num
            count += 1
        avg_num = total / count

print(f"максимальное число: {max_num}, минимальное число: {min_num}, среднее значение: {avg_num}")

