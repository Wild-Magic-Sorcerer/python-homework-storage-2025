def big_One(def_for_big):
    great_One = int(split_of_numb[0])
    for i in split_of_numb:
        a1 = int(i)
        if a1 > great_One:
            great_One = a1
    return great_One


def little_One(def_for_little):
    small_One = int(split_of_numb[0])
    for d in split_of_numb:
        a2 = int(d)
        if a2 < small_One:
            small_One = a2
    return small_One

if __name__ == "__main__":
    user_input = input("Введите числа через пробел")
    split_of_numb = user_input.split(" ")
    if len(split_of_numb) <= 10:
        print(split_of_numb)
    else:
        print("Вы ввели не число.")
    z_list = [0]
    for v in split_of_numb:
        a3 = int(v)
        z_list = [z_list[0] + a3]
        print(big_One(split_of_numb), little_One(split_of_numb), z_list)
