def polyndrom_check(words=str):
    words.replace(' ', '')
    for i in range(int(len(words) / 2)):
        if words[i] != words[len(words) - i - 1]:
            return print(f'Строка не является полиндромом начиная с {i + 1} буквы с любой стороны')
    return print("Это полиндром")

if __name__ == '__main__':
    polyndrom_check(input("Напишите полиндром:\n"))

