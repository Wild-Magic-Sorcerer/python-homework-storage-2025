def even_and_odd_num (arg):
    if not arg:
        return None
    even_list =[]
    odd_list = []
    for num in arg:
        if num % 2 == 0:
            even_list.append(num)
        elif num % 2 != 0:
            odd_list.append(num)
    return even_list, odd_list

if __name__ == '__main__':
    list_of_num = [1,2,3,4,5,6,7,8,9,10]
    even, odd = even_and_odd_num(list_of_num)

    print(f"Список четных чисел:{even}\nСписок нечетных чисел:{odd}")

