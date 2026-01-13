def get_sums(numbers):
    even_sum = sum(n for n in numbers if n % 2 == 0)
    odd_sum = sum(n for n in numbers if n % 2 != 0)
    return odd_sum, even_sum

def main():
    
    # Основная программа
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum_o, sum_e = get_sums(nums)
    
    print("--- Результаты расчёта ---")
    print(f"Сумма нечётных чисел: {sum_o}")
    print(f"Сумма чётных чисел:   {sum_e}")
    
    print("-" * 26)

if __name__ == "__main__":
    main()


