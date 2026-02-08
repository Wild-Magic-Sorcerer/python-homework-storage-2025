def multiply_int(*args):
    result = 1
    found_int = False

    for arg in args:
        if type(arg) is int:
            result *= arg
            found_int = True

    if found_int:
        return result
    else:
        return None
