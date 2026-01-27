import re

def sorting(list_num):
    countr = []
    town = []
    person = []
    for numer in list_num:
        countr.append(numer[1])
        town.append(numer[3:6])
        person.append(numer[7:])
    return countr,town,person

if __name__ == '__main__':
    line = input('Введите пожалуйста номер телефона:\n')
    result = re.findall(r'\+\d\(\d{3}\)\d{3}-\d{2}-\d{2}', line)
    if result is None:
        print("Номер не найден")
    else:
        check = sorting(result)
        print(f'Код страны номера/ов: {check[0]}\nКод города номера/ов: {check[1]}\nПерсональный код номера/ов: {check[2]}')
