def main():
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
        user_input = input("Введите число, которое нужно возвести в квадрат: ")
        
        val = float(user_input)
    except ValueError:
        # Обработка ошибки, если пользователь ввел буквы вместо цифр
        print("Ошибка! Пожалуйста, вводите только числа.")
    except Exception:
        print("Произошла иная ошибка")
    else:
        final_result = get_square(val)
        print(f"Результат вычислений: {final_result}")
        

if __name__ == "__main__":
    main()

