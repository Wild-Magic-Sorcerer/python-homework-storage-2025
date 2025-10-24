def polyndrom_check(words: str):
    words.replace(' ', '')
    for i, j in zip(words, reversed(words)):
        if i != j:
            return print(f'Строка не является полиндромом начиная с {i} буквы с левой стороны')
    return print("Это полиндром")

if __name__ == '__main__':
    polyndrom_check(input("Напишите полиндром:\n"))
