ten_random_number: list = ['6','8','1','-3','12','3','6','55','9','0']
name_faila = 'numbers.txt'

def number_chek(num: list):
    max_num = max(int(i) for i in num)
    min_num = min(int(i) for i in num)
    sum_num = sum(int(i) for i in num)/len(num)
    return min_num,max_num,sum_num

if __name__ == '__main__':
    with open(name_faila,'w') as numbers:
        for num in ten_random_number:
            numbers.write(num + '\n')

    with open(name_faila) as num_line:
        list_number = num_line.readlines()

    min_num_list, max_num_list, sum_num_list = number_chek(list_number)
    print(f'MAX: {max_num_list}\nmin: {min_num_list}\nСреднее значение: {sum_num_list}')
