def my_decorator(func):
    def wrapper(a, b):
        print("Выполняется функция...")
        res = func(a, b)
        print("Функция выполнена")
        return res
    return wrapper
@my_decorator
def add(a, b):
    return a + b
result = add(1, 2)
print(f"Итог, {result}")
