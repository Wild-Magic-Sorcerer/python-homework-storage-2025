def factorial_iterative(number):

    if not isinstance(number, int):
        return None
    if number < 0:
        return None
    result = 1
    for num in range(1, number + 1):
        result *= num
    return result


def factorial_recursive(number):

    if not isinstance(number, int):
        return None
    if number < 0:
        return None
    if number <= 1:
        return 1
    return number * factorial_recursive(number - 1)

if __name__ == '__main__':
    print(factorial_iterative(6))
    print(factorial_recursive(5))
