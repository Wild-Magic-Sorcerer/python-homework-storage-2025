def main():
    check_parity = lambda x: x % 2 == 0
    print(f"{'Число':<10} | {'Чётное?':<10} | {'Результат лямбды':<15}")
    print("-" * 45)

    for i in range(1, 11):
        is_even = check_parity(i)
        status = "Да" if is_even else "Нет"
   
        print(f"{i:<10} | {status:<10} | {str(is_even):<15}")

if __name__ == "__main__":
    main()
    
