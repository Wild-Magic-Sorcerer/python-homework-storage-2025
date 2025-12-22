import re

if __name__== "__main__":
    text = input("Введите строку с датами в формате ДД.ММ.ГГГГ: ")
    result = re.sub(r'\d{2}.\d{2}.\d{4}', 'DD.MM.YYYY', text)
    print("Результат замены:", result)
