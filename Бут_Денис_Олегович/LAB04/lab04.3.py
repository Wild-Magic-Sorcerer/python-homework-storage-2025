from functools import reduce

function_of_multiplying = lambda x, y: x * y

if __name__ == "__main__":
    list_from_1_to_10 = list(range(1,11))
    multiplying = reduce(function_of_multiplying, list_from_1_to_10)
    print(multiplying)


