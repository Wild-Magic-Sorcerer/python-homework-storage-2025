def sum_odd_even(list_num: list):
    odd: int = 0
    even: int = 0
    for num in list_num:
        if num%2 == 0:
            even += num
        else:
            odd += num
    return odd,even

if __name__ == '__main__':
    print("Введите числа для суммирования\nКогда закончите введите n")
    numers = []
    while True:
        numer = input('Введите число: ')
        if 'n' == numer.lower():
            break
        try:
            numers.append(int(numer))
        except ValueError:
            print("Ошибка это не число")

    sum_odd, sum_even = sum_odd_even(numers)
    print(f'Сумма нечётных цифр = "{sum_odd}"\nСумма чётных цифр = "{sum_even}"')
