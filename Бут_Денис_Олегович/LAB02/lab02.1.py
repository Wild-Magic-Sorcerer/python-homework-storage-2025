def palindrome(some_str):
    if not some_str:
        return None

    some_str = some_str.lower().replace(" ", "")

    if some_str == some_str[::-1]:
        return True

    for num in range(len(some_str) // 2):
        if some_str[num] != some_str[-num - 1]:
            print(f"Различие на позиции {num}: '{some_str[num]}' != '{some_str[-num - 1]}'")
            return None
    return None

if __name__ == "__main__":
    string = input("Введите строку: ")

    if palindrome(string):
        print("Это палиндром!")
    else:
        print("Это не палиндром.")