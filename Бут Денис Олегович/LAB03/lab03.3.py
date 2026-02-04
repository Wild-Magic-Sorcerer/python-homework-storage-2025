def multiplying_args(*args):
    if not args:
        return None

    numbers = [arg for arg in args if type(arg) == int]

    result = 1
    intermediate = []
    for num in numbers:
        result = result * num
        intermediate.append(result)

    return result, intermediate
if __name__ == "__main__":
    list_for_def = [True,1,"ss",2,(1,4),4]
    print(multiplying_args(*list_for_def))
