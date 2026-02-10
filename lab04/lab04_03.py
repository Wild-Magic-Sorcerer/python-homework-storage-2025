# Дан список чисел от 1 до 10
# Используйте функцию reduce (из модуля functools) и лямбда-функцию, чтобы найти произведение всех элементов списка.

from functools import reduce as rd

if __name__ == '__main__':
    our_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l = lambda x, y: x + y
    print(rd(l, our_list))
