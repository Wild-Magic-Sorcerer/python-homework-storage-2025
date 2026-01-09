def main():
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, help="Число для расчета факториала")
    parser.add_argument("-v", "--verbose", action="store_true", help="Подробный режим")
    
    args = parser.parse_args()
    
    n = args.n
    result = 1
    
    if args.verbose:
        print(f"Начинаем расчет факториала для числа {n}:")
    
    for i in range(1, n + 1):
        old_res = result
        result *= i
        if args.verbose:
            print(f"Шаг {i}: {old_res} * {i} = {result}")
    
    if not args.verbose:
        print(f"Результат: {result}")
    else:
    
        print(f"Итоговый ответ: {result}")
        
if __name__ == "__main__":
    main()

