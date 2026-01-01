import sys

def calculator (some_list):
    if len(some_list) >= 4:
        num1, operation, num2 = int(some_list[1]), some_list[2], int(some_list[3])

        operations = {"add": ("+", num1 + num2),
                      "sub": ("-", num1 - num2),
                      "mul": ("*", num1 * num2),
                      "div": ("/", num1 / num2),
                      }
        if operation in operations:
            op, result = operations[operation]
            return f" Результат вычеслений = {result} "
        else:
            return f"Ввод некоректной операции"
    elif 3 <= len(some_list) < 4:
        num1, num2 = int(some_list[1]), int(some_list[2])
        return f"Ваши числа: {num1}, {num2}"
    return None

if __name__ == "__main__":
    print(calculator(sys.argv))