def main():
    def multiply_ints(*args):
        integers = [x for x in args if isinstance(x, int)]
        
        if not integers:
            return None
        
        res = 1
        for n in integers:
            res *= n
        return res
    
    # Проверяем
    print(f"Результат с числами: {multiply_ints(2, 'текст', 3, 4.5, 10)}")
    
    print(f"Результат без целых: {multiply_ints('привет', 0.5)}")

if __name__ == "__main__":
    main()


