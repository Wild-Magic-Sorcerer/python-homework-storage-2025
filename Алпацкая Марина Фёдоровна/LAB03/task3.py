def product_of_numbers(*args):
    result:int =1
    temp = 1
    for iteratcy in args:
        try:
            result *= int(iteratcy)
            temp = 0
        except ValueError:
            continue
    if temp == 0:
        return result
    return None

if __name__ == '__main__':
    product_numbers = product_of_numbers(32,6,"hjfg")
    print(f'Произведение целочисленных аргументов = "{product_numbers}"')