def notification_decorator(func):

    def wrapper(*args, **kwargs):
        print("Выполняется функция...")
        result = func(*args, **kwargs)
        print("Функция выполнена.")
        return result
    return wrapper

@notification_decorator
def square_number(n):
    return n ** 2

if __name__ == "__main__":
    print("Результат:", square_number(2))
    print("Результат:", square_number(3))
