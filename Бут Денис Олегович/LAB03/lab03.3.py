def multiplying_args(*args):
    if not args:
        return None

    numbers = [arg for arg in args if isinstance(arg, int) and not isinstance(arg, bool)]

    result = 1
    intermediate = [result := result * num for num in numbers]

    return numbers, intermediate
if __name__ == "__main__":
    list_for_def = [False,1,"ss",2,(1,4),4]
    print(multiplying_args(*list_for_def))
