def main():

    numbers = [1, 2, 3, 2, 4, 1, 5, 2, 3, 1, 4, 4, 5]

    frequency = {}

    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    print("Число - Количество:")
    for num, count in sorted(frequency.items()):
        print(f"{num} — {count}")

if __name__ == "__main__":
    main()
