if __name__ == "__main__":
    list_to_ten = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_comprehensions = [number for number in list_to_ten if number % 3 == 0]
    print(list_comprehensions)
