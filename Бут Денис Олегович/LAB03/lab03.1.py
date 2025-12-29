def average (list_of_strings):
    list_of_lens = []
    for string in list_of_strings:
        list_of_lens.append(len(string))
    avg = sum(list_of_lens) // len(list_of_lens)
    return avg


def average_string (list_of_strings, number=0 ):
    for string in list_of_strings:
        if len(string) < number:
            list_of_strings.remove(string)
    return list_of_strings


if __name__ == "__main__":
    list_of_str = ["first string", "second", "third string", "fourth"]
    num = average(list_of_str)
    print(f" Строки большие чем среднее значение:{average_string(list_of_str, num)}")

