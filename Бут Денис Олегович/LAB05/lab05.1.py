def calculate_big_one(def_for_big_num):
    if not def_for_big_num:
        return None
    biggest_num = int(def_for_big_num[0])
    for num in def_for_big_num:
        if num > biggest_num:
            biggest_num= num
    return biggest_num


def calculate_little_one(def_for_smallest_num):
    if not def_for_smallest_num:
        return None
    smallest_num = int(def_for_smallest_num[0])
    for num in def_for_smallest_num:
        if num < smallest_num:
            smallest_num = num
    return smallest_num

def average(some_list):
    if not some_list:
        return None
    return sum(some_list) / len(some_list)




if __name__ == "__main__":
    list_of_numbs = []
    with open("numbers_for_lab05.1.txt", "r") as file_numbers:
        for line in file_numbers:
             try:
                value = int(line)
                list_of_numbs.append(value)
            except ValueError:
                print("Value is not an integer")
        print(list_of_numbs)
        print( "Наибольшее число =",calculate_big_one(list_of_numbs),"\n"
               "Наименьшее число =",calculate_little_one(list_of_numbs),"\n"
               "Среднее чисел =",average(list_of_numbs))

