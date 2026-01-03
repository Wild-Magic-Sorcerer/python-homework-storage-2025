def filter_long_strings(strings):
    if not strings:
        return []
    
    # Считаем среднюю длину: сумма длин всех строк / количество строк
    avg_length = sum(len(s) for s in strings) / len(strings)
    
    # Собираем в новый список те, что длиннее средней
    result = [s for s in strings if len(s) > avg_length]
    return result

# Тестик
test_list = ["я", "учу", "вышмат", "в", "политехе"]
print(f"Строки длиннее средней: {filter_long_strings(test_list)}")