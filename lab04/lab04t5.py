def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def square(x):
    return x ** 2

print("Выполняется функция...")

user_input = input("Введите число для вычисления квадрата: ")

try:
    number = float(user_input)
    result = square(number)
    print(f"Функция выполнена.")
    print(f"Результат: {result}")
except ValueError:
    print("Пожалуйста, введите корректное число.")