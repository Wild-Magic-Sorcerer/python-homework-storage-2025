import argparse
if __name__ == '__main__':
    calculat = argparse.ArgumentParser(description='Считает факториал')
    calculat.add_argument('num', type=int)
    calculat.add_argument('-d','--details')
    factorial = calculat.parse_args()

    calculation: int = 1
    for i in range(factorial.num - 1):
        if factorial.details:
            print(f'Считаем по порядку: {calculation} * {factorial.num - i}')
        calculation *= factorial.num - i


    print(f'Фактариал равен = {calculation}')