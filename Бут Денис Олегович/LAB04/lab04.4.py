
parity_function = lambda x: x % 2 == 0

function_for_5 = lambda x: x >= -5


if __name__ == "__main__":
    result_of_function = []
    list_of_numbers = [-8, -12, -20, -4, 9, -15, -9, 11, -6, -1, -14, 13, 14, 4, -18,
                       -7, -10, -13, 12, -2, 10, -5, -11, 18, 6, -17, 17, 8, 16, 19,
                       3, -16, 0, 1, -3, 5, 7, 2, -19, 15]
    correct_values = filter(parity_function, list_of_numbers)
    correct_values = filter(function_for_5, list(correct_values))
    print(list(correct_values))

