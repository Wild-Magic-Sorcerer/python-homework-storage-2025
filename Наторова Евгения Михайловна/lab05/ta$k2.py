fil = "pupa.txt"

if __name__ == "__main__":
    user_input = input("ввидите строку: ")

    with open(fil, "a") as file:
        file.write(user_input + "\n")

    with open(fil, "r") as file:
        print(file.read())
