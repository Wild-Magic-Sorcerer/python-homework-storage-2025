if __name__ == '__main__':
    parity = lambda x: True if x%2 == 0 else False
    while True:
        num = input(f'Введите число: ')
        try:
            num_int = int(num)
            break
        except ValueError:
            print('Вы ввели не целочисленное значение, пожалуйста попробуйте снова')

    print(parity(num_int))
