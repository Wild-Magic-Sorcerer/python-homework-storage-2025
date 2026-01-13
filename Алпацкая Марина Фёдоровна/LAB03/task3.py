def product_of_numbers(*args):
    result:int =1
    num_list = [num_int for num_int in args if isinstance(num_int, int)]
    if not num_list:
        return None
    for iteratcy in num_list:
        result *= iteratcy
    return result


if __name__ == '__main__':
    product_numbers = product_of_numbers(32,6,"hjfg")
    print(f'Произведение целочисленных аргументов = "{product_numbers}"')
