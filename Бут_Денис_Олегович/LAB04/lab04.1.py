parity_function = lambda x: x % 2 == 0


if __name__ == "__main__":
    result = []
    for function_argument in range(1, 100):
        result.append(parity_function(function_argument))
    print('Делящиеся на 2 без остатка:', result)
