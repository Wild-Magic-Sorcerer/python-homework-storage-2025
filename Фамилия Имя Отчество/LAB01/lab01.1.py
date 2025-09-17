Numb = input("Напишите числа через пробел")
split_of_numb = Numb.split(" ")
Z_list = [0]
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

print(big_One(split_of_numb), little_One(split_of_numb), Z_list)
if __name__ == "__main__":
    ...
