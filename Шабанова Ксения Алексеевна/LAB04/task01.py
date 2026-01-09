def main():
    # Создаем лямбду
    is_even = lambda x: x % 2 == 0
    
    # Проверяем в диапазоне от 1 до 10
    for i in range(1, 11):
    
        print(f"Число {i}: {is_even(i)}")
        
if __name__ == "__main__":
    main()


