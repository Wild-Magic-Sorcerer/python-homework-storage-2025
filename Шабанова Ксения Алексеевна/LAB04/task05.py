def trace_decorator(func):
    def wrapper(n):
        print("Выполняется функция...")
        result = func(n)
        print("Функция выполнена.")
        return result
    return wrapper

@trace_decorator
def get_square(number):
    return number ** 2

# Основная часть программы с вводом
try:
    # Просим пользователя ввести число
    user_input = input("Введите число, которое нужно возвести в квадрат: ")
    
    # Преобразуем ввод в число
    val = float(user_input)
    
    # Вызываем нашу декорированную функцию
    final_result = get_square(val)
    
    print(f"Результат вычислений: {final_result}")

except ValueError:
    # Обработка ошибки, если пользователь ввел буквы вместо цифр
    print("Ошибка! Пожалуйста, вводите только числа.")