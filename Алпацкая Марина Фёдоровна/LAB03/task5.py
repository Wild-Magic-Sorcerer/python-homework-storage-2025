def iter_factorial(numer: int):
    calculation: int = 1
    for i in range(numer-1):
        calculation *= numer-i
    return calculation

def recursive_factorial(num: int):
    if num<=1:
        return 1
    return num*recursive_factorial(num-1)

if __name__ == '__main__':
    while True:
        factorial_num = input(f'Введите число для подсчёта факториала\n')
        try:
            num = int(factorial_num)
            break
        except ValueError:
            print('Вы ввели не целочисленное значение, пожалуйста попробуйте снова')

    factorial_i = iter_factorial(int(factorial_num))
    factorial_r = recursive_factorial(int(factorial_num))
    print(f'Фактариал подсчитаный индуктивной функцией: {factorial_i}\nФактариал подсчитаный рекурсивной функцией: {factorial_r}')
