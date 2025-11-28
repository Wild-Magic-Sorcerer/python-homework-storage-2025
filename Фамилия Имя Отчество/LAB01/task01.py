if __name__ == '__main__':
    number = []
    while len(number) < 10:
        temp = input("введите число: ")
        try:
            temp_int = int(temp)
            number.append(int(temp))
        except ValueError:
            print("ошика")
    if number:
        maxi = number[0]
        mini = number[0]
        total = 0
        for num in number:
            if num > maxi:
                maxi = num
            if num < mini:
                mini = num
            total += num

        print(f'maximum: {maxi}, minimum: {mini}, summa: {total}')
    else:
        print('pusto')
