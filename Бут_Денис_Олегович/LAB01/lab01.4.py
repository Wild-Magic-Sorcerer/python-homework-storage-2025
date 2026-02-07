if __name__ == "__main__":
    main_list = [1, 4, 8, 11, 31, 8, 32, 324, 8]
    tuple_of_num = {}
    for number in main_list:
        amount_of_number = main_list.count(number)
        if number not in tuple_of_num:
            tuple_of_num.update({number: amount_of_number})
        else:
            continue
    print(tuple_of_num)
