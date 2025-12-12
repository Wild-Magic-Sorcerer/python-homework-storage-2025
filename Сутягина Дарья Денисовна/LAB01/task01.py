def get_numbers_from_user():
    num_in = []
    while len(num_in) < 10:
        user_input = input('Введите целое число: ')
        try:
            num = int(user_input)
            num_in.append(num)
        except ValueError:
            print('Это не целое число, попробуйте снова.')
    return num_in


def find_min(numbers):
    if not numbers:
        raise ValueError("Список чисел пуст.")
    minimum = numbers[0]

    for num in numbers[1:]:
        if num < minimum:
            minimum = num
    return minimum


def find_max(numbers):
    if not numbers:
        raise ValueError("Список чисел пуст.")
    maximum = numbers[0]

    for num in numbers[1:]:
        if num > maximum:
            maximum = num
    return maximum


def sum_numbers(nums):
    if not nums:
        raise ValueError("Список чисел пуст.")    
    total = 0
    for num in nums:
        total += num
    return total

    
if __name__ == '__main__':
    numbers = get_numbers_from_user()
    print('Минимальное число:', find_min(numbers))
    print('Максимальное число:', find_max(numbers))
    print('Сумма всех чисел:', sum_numbers(numbers))
