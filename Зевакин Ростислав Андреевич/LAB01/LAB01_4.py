def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 1, 5, 7, 3, 2, 6, 4, 1, 3, 2, 7, 5]

    count_dict = {}
    for num in numbers:
        count_dict[num] = count_dict.get(num, 0) + 1

    print("Всего повторов:")
    for num in sorted(count_dict.keys()):
        print(f"{num}: {count_dict[num]}")

if __name__ == '__main__':
    main()
    
