import random

if __name__ == '__main__':
    random_list = random.sample(range(-20,21), 10)
    filtr_randoma  = list(filter(lambda num: (num > -5 and num%2 == 0) , random_list))
    print(filtr_randoma)
    print(random_list)
