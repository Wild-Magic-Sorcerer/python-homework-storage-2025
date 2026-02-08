def multiplying_args(*args):
    if not args:
        return None

    numbers = [arg for arg in args if type(arg) == int]
    if not numbers:
        return None

    result = 1
    for num in numbers:
        result = result * num

    return result

if __name__ == "__main__":
    list_for_def = [True,1,"ss",2,(1,4),4]
    print(multiplying_args(*list_for_def))

