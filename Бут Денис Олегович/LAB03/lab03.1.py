def average(list_of_strings):
    avg = sum([len(string) for string in list_of_strings]) / len(list_of_strings)
    return avg


def average_string(list_of_strings, number = None ):
    list_of_strings = [ string for string in list_of_strings if len(string) > number ]
    return list_of_strings


if __name__ == "__main__":
    list_of_str = ["first string", "second", "third string", "fourth"]
    num = average(list_of_str)
    print(f" Строки большие чем среднее значение:{average_string(list_of_str, num)}")

