def find_min(numbers_list):
    if not numbers_list:
        return None
        
    for num in numbers_list:
        if num < current_min:
            current_min = num
    return current_min

def find_max(numbers_list):
    if not numbers_list:
        return None
    current_max = numbers_list[0]
    
    for num in numbers_list:
        if num > current_max:
            current_max = num
            
    return current_max

def main():
    numbers = []
    print("Введите 10 целых чисел:")
    
    while len(numbers) < 10:
        user_input = input(f"Введите число №{len(numbers) + 1}: ")
        
        try:
            num = int(user_input)
            numbers.append(num)
        except ValueError:
            print("Ошибка: пожалуйста, введите корректное целое число.")

    min_val = find_min(numbers)
    max_val = find_max(numbers)
    total_sum = sum(numbers)

    print("-" * 30)
    print(f"Ваш список: {numbers}")
    print(f"Минимальное число (ручной поиск): {min_val}")
    print(f"Максимальное число (ручной поиск): {max_val}")
    print(f"Сумма всех чисел: {total_sum}")

if __name__ == "__main__":
    main()
    
