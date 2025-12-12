def decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is executing")
        func(*args, **kwargs)
        print("function is executed")
    return wrapper


@decorator
def square_of_numb(number):
    square = number**2
    print(square)

if __name__ == "__main__":
    square_of_numb(10)
