list_numbers = [6, 7, 8, 6, 5, 64, 4, 5, 6, 7, 6, 6, 5, 4, 5]

if __name__ == '__main__':
    dictionaries_number = {}

    for i in list_numbers:
        if i not in dictionaries_number:
            dictionaries_number[i] = list_numbers.count(i)

    for key in dictionaries_number:
        print(f"Число '{key}' встречается: {dictionaries_number.get(key)} раз")

