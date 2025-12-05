def decorator_square(decor_f):
    def wrapper(x):
        print("Выполняется функция...")
        print(decor_f(x))
        print("Функция выполнена.")
        return decor_f(x)
    return wrapper

@decorator_square
def square(num: int):
    return num**2

if __name__ == '__main__':
    numer = input(f'Введите число: ')
    result = square(int(numer))
    print(f'Квадрат вашего числа: {result}')
