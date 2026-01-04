def calculate_big_one(def_for_big_num):
    biggest_num = int(def_for_big_num[0])
    for num in def_for_big_num:
        if int(num) > biggest_num:
            biggest_num= int(num)
    return biggest_num


def calculate_little_one(def_for_smallest_num):
    if not def_for_smallest_num:
        return None
    smallest_num = int(def_for_smallest_num[0])
    for num in def_for_smallest_num:
        if int(num) < smallest_num:
            smallest_num = int(num)
    return smallest_num

if __name__ == "__main__":
    list_of_num = []
    while len(list_of_num) <= 9:
        user_numbers = input("Введите числа")
        if user_numbers.lower() == "n" or user_numbers == "":
            break
        list_of_num.append(user_numbers)
    print(list_of_num)
    list_for_sum = [0]
    for number in list_of_num:
        list_for_sum = [list_for_sum[0] + int(number)]
    print(calculate_big_one(list_of_num), calculate_little_one(list_of_num), list_for_sum)
