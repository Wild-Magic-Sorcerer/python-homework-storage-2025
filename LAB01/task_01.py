TARGET_COUNT = 10


def collect_numbers(required_count: int) -> list[int]:
    collected: list[int] = []
    while len(collected) < required_count:
        remaining = required_count - len(collected)
        user_input = input(f"Введите целое число (осталось {remaining}): ").strip()
        try:
            num = int(user_input)
            collected.append(num)
        except ValueError:
            print("Ошибка: введите корректное целое число")
    return collected


def calculate_statistics(values: list[int]) -> tuple[int, int, int]:
    if not values:
        raise ValueError("Список не может быть пустым")
    return min(values), max(values), sum(values)


def main() -> None:
    number_list = collect_numbers(TARGET_COUNT)
    minimum, maximum, total = calculate_statistics(number_list)
    
    print(f"\nВведённые числа: {number_list}")
    print(f"Минимальное: {minimum}")
    print(f"Максимальное: {maximum}")
    print(f"Сумма: {total}")


if __name__ == "__main__":
    main()
