def filter_kwargs_by_vowels(**kwargs):
    vowels = "аеёиоуыэюяaeiouy"
    result = {}
    
    for key, value in kwargs.items():
        # Проверяем, что значение — строка
        if isinstance(value, str):
            # Считаем гласные в этой строке
            count = sum(1 for char in value.lower() if char in vowels)
            if count >= 3:
                result[key] = value
                
    return result

def main():
    
    # Пример
    res = filter_kwargs_by_vowels(name="Настя", job="учитель", city="Москва", fruit="апельсин")
    
    print(f"Подходящие аргументы: {res}")

if __name__ == "__main__":
    main()


