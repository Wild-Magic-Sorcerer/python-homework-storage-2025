def multiply_integers(*args):
    result = None
    for arg in args:
        if isinstance(arg, int) and not isinstance(arg, bool):
            if result is None:
                result = arg
            else:
                result = result * arg
    return result
print(multiply_integers(2, 'какой-то текст', 3.5, 4))
print(multiply_integers('бла бла', True, 5.0))
