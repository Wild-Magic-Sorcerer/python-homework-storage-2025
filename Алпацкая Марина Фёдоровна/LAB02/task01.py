def number_chek(num: list):
    max_num = max(i for i in num)
    min_num = min(i for i in num)
    sum_num = sum(i for i in num)
    return min_num,max_num,sum_num

if __name__ == '__main__':
    number = []
    while len(number) < 10:
        temp = input("введите число: ")
        try:
            number.append(int(temp))
        except ValueError:
            print("Пожалуйста введите число")
    print(f'MAX: {number_chek(number)[1]}\nmin: {number_chek(number)[0]}\nСумма всех чисел: {number_chek(number)[2]}')
