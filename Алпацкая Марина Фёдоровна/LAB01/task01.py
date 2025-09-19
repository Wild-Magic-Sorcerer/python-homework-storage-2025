

if __name__ == '__main__':
    number = []
    while len(number) < 10:
        temp = input("введите число: ")
        try:
            temp_int = int(temp)
            number.append(int(temp))
        except ValueError:
            print("Пожалуйста введите число")
    print(max(i for i in number))
    print(min(i for i in number))
    print(sum(i for i in number))
