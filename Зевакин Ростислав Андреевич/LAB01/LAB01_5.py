def main():
    numbers = list(range(-10, 11))

    multiples_of_3 = [num for num in numbers if num % 3 == 0]

    print(f"\nИсходный список ({len(numbers)} чисел):")
    print(numbers)

    print(f"\nЧисла, кратные 3 ({len(multiples_of_3)} чисел):")
    print(multiples_of_3)

    print(f"\nМинимальное кратное: {min(multiples_of_3)}")
    print(f"Максимальное кратное: {max(multiples_of_3)}")


if __name__ == "__main__":
    main()
  
