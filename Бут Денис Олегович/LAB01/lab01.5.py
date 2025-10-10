if __name__ == "__main__":
    main_list = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_list = [x for x in main_list if x % 3 == 0]
    print(new_list)
