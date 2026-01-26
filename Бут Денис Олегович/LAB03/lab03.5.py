def factorial(number):
    if not number:
        return None
    if isinstance(number,int):
        result = 1
        for num in range(1,number + 1):
            result *= num
        return result
    return None

def factorial_rec(number):
    if not isinstance(number,int) or not number:
        return None
    if number == 0 or number == 1:
        return 1
    return number * factorial_rec(number - 1)

if __name__ == '__main__':
    print(factorial(6))
    print(factorial_rec(5))



