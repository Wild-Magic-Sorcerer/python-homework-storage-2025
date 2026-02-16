def sum_even_odd(numbers: list):
    even_sum = 0
    odd_sum = 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return even_sum, odd_sum

def main():
    user_input = input("Введите числа через пробел: ")
    numbers = list(map(int, user_input.split()))
    even, odd = sum_even_odd(numbers)

    print("Сумма чётных:", even)
    print("Сумма нечётных:", odd)

if __name__ == "__main__":
    main()
