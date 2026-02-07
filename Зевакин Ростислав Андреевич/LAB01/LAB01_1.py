numbers = []

print('Введите 10 целых чисел:')

for i in range(10):
    while True:
        try:
            num = int(input(f'Число {i +1}: '))
            numbers.append(num)
            break
        except ValueError:
            print("Введено неверное число")

print(f'min: {min(numbers)}, max: {max(numbers)}, sum: {sum(numbers)}')