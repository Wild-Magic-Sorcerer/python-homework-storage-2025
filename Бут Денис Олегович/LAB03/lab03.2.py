
if __name__ == '__main__':
    list_of_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even = [num for num in list_of_num if num % 2 == 0]
    odd = [num for num in list_of_num if num % 2 != 0]

    print(f"Список четных чисел: {even}")
    print(f"Список нечетных чисел: {odd}")

