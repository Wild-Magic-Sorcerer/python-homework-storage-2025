def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Выполняется функция...")
        result = func(*args, **kwargs)
        print("Функция выполнена.")
        return result
    return wrapper

def square_number(n):
    return n ** 2

def main():
    number = 5
    print(f"--- Старт программы для числа {number} ---")
    final_result = square_number(number)
    
    print(f"Результат вычислений: {final_result}")

if __name__ == "__main__":
    main()
