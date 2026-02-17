def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Выполняется функция...")
        result = func(*args, **kwargs)
        print("Функция выполнена.")
        return result
    return wrapper

@simple_decorator
def square(x):
    return x * x

@simple_decorator
def greet(name):
    return f"Здравствуй, {name}!"

@simple_decorator
def add(a, b):
    return a + b

print("Демонстрация работы декоратора:")

print("1. Вычисление квадрата числа 5:")
result = square(5)
print(f"Результат: {result}")

print("2. Приветствие пользователя:")
result = greet("Борька")
print(f"Результат: {result}")

print("3. Сложение чисел 3 и 4:")
result = add(3, 4)
print(f"Результат: {result}")

import datetime

@simple_decorator
def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

print("4. Получение текущего времени:")
time_str = get_current_time()
print(f"Текущее время: {time_str}")