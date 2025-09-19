numb = []
while len(numb) < 10:
    user_input = input("Введите число")
    if user_input.isdigit():
        numb.append(user_input)
    else:
        print("Вы ввели не число.")
split_of_numb = numb.split(" ")
z_list = [0]
print(split_of_numb)


def big_One(split_of_numb):
    great_One = int(split_of_numb[0])
    for i in split_of_numb:
        a1 = int(i)
        if a1 > great_One:
            great_One = a1
    return great_One


def little_One(split_of_numb):
    small_One = int(split_of_numb[0])
    for d in split_of_numb:
        a2 = int(d)
        if a2 < small_One:
            small_One = a2
    return small_One


for v in split_of_numb:
    a3 = int(v)
    Z_list = [Z_list[0] + a3]

if __name__ == "__main__":
    numb = []
    while len(numb) < 10:
        user_input = input("Введите число")
    if user_input.isdigit():
        numb.append(user_input)
    else:
        print("Вы ввели не число.")
    split_of_numb = numb.split(" ")
    z_list = [0]
    print(split_of_numb)
    print(big_One(split_of_numb), little_One(split_of_numb), z_list)
