import random
from typing import List


def generate_random_numbers(start: int = -10, end: int = 10,
                            count: int = 10) -> List[int]:

    possible_numbers = list(range(start, end + 1))

    return random.sample(possible_numbers, k=count)


def find_multiples(numbers: List[int], divisor: int = 3) -> List[int]:

    return [num for num in numbers if num % divisor == 0]


def print_statistics(numbers: List[int], multiples: List[int],
                     divisor: int = 3) -> None:

    print(f"\n1. Сгенерированные числа ({len(numbers)} шт.):")
    print(f"   {sorted(numbers)}")

    print(f"\n2. Все числа от -10 до 10 (диапазон):")
    print(f"   {list(range(-10, 11))}")

    print(f"\n3. Числа, кратные {divisor}:")
    if multiples:
        print(f"   {sorted(multiples)}")
        print(f"\n   Найдено: {len(multiples)} число(ел)")

        percentage = (len(multiples) / len(numbers)) * 100
        print(f"   Это {percentage:.1f}% от всех сгенерированных чисел")
    else:
        print(f"   Числа, кратные {divisor}, не найдены")

def main() -> None:
    random_numbers = generate_random_numbers(start=-10, end=10, count=10)

    multiples_of_3 = find_multiples(random_numbers, divisor=3)

    print_statistics(random_numbers, multiples_of_3, divisor=3)


if __name__ == "__main__":
    main()
