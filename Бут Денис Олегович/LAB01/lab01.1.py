def calculate_big_One(def_for_big):
    great_One = int(def_for_big[0])
    for i in def_for_big:
        a1 = int(i)
        if a1 > great_One:
            great_One = a1
    return great_One


def calculate_little_One(def_for_little):
    if not def_for_little:
        return None
    small_One = int(def_for_little[0])
    for d in def_for_little:
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
        print(calculate_big_One(split_of_numb), calculate_big_One(split_of_numb), z_list)
