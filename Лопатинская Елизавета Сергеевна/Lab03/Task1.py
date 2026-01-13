def filter_long_strings(strings_list):
    if not strings_list:
        return []

    avg_length = sum(len(s) for s in strings_list) / len(strings_list)
    print(f"Средняя длина строки: {avg_length:.2f}")

    result = [s for s in strings_list if len(s) > avg_length]
    return result

def main():
    print("--- Программа отбора строк по средней длине ---")    
    words = ["яблоко", "дом", "программирование", "код", "питон"]
    print(f"Исходный список: {words}")
    filtered = filter_long_strings(words)
    print(f"Строки длиннее средней: {filtered}")
    print("-" * 50)

if __name__ == "__main__":
    main()

