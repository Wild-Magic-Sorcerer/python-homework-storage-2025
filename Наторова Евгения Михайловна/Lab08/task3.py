import re

if __name__== "__main__":
    text = input("Введите строку для разбития на слова в формат: ")
    result = re.split(r'[.,!?-]', text)
    print("Список слов без пустых элементов:", result)


