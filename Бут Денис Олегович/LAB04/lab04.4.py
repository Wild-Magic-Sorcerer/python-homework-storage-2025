import random
parity_function = lambda x: x % 2 == 0

function_for_5 = lambda x: x >= -5


if __name__ == "__main__":
    result_of_function = []
    list_of_numbers = list(range(-20,20))
    random.shuffle(list_of_numbers)
    print(list_of_numbers)
    correct_values = filter(parity_function, list_of_numbers)
    correct_values = filter(function_for_5, correct_values)
    print(list(correct_values))
