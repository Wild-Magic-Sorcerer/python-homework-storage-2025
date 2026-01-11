def sum(numbers):
    sumnech = 0
    sumch = 0

    for num in numbers:
        if num % 2 == 0:
            sumch += num
        else:
            sumnech += num

    return sumnech, sumch

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    (nech, ch) = sum(numbers)
    print(f"Сумма нечётных чисел {nech}, сумма чётных чисел {ch}")
