if __name__ == "__main__":
    numbers = [4, 1, 9, 3, 4, 1, 2, 6, 8, 9, 1]

    dict = {}

    for num in numbers:
        dict[num] = dict.get(num, 0) + 1

    for number, count in sorted(dict.items()):

        print(f"  {number} — {count}")
        
