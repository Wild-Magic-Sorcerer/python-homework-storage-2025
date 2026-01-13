def polyndrom_check(words: str):
    words.replace(' ', '')
    for i, j in zip(words, reversed(words)):
        if i != j:
            return f'Строка не является полиндромом начиная с {i} буквы с левой стороны'
    return f"Это полиндром"

if __name__ == '__main__':
    result_polindrom = polyndrom_check(input("Напишите полиндром:\n"))
    print(result_polindrom)
