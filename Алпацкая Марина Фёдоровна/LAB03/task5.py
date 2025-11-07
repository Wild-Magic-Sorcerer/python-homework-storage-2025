def iter_factorial(numer: int):
    calculation : int = 0
    for i in range(numer):
        calculation += numer-i
    return calculation

def recursive_factorial(num: int, fact:list = [1]):
    if not len(fact) == num:
        fact.append(len(fact)*(len(fact)+1))
        recursive_factorial(num, fact)
    return fact[len(fact)-1]

if __name__ == '__main__':
    factorial_num = input(f'Введите число для подсчёта факториала')
    factorial_i = iter_factorial(int(factorial_num))
    factorial_r = recursive_factorial(int(factorial_num))
    print(factorial_i, factorial_r)
