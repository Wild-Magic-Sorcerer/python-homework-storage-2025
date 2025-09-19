def main():

    numbers = list(range(-10, 11))

    multiples_of_3 = [x for x in numbers if x % 3 == 0]

    print(f"Исходный список: {numbers}")
    print(f"Числа, кратные 3: {multiples_of_3}")

if __name__ == "__main__":
    main()
