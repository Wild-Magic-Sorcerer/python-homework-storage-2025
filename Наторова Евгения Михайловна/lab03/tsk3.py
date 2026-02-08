def multiint(*args):
    integers = [arg for arg in args if isinstance(arg, int)]
    if not integers:
        return None
    result = 1
    
    for num in integers:
        result *= num

    return result

if __name__ == "__main__":
    result1 = multiint(5, 3, 'gegf', 4.5, [1,2,3])
    result2 = multiint( 'лупа', "чайник", [1, 2, 3])

    print(result1, result2)
    
