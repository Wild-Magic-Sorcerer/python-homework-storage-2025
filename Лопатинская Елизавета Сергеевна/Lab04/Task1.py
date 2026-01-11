def check_parity(x):
    return x % 2 == 0

def main():
    print(f"{'Число':<10} | {'Чётное?':<10}")
    print("-" * 25)

    for i in range(1, 11):
        is_even = check_parity(i)
        status = "Да" if is_even else "Нет"
        print(f"{i:<10} | {status:<10}")

if __name__ == "__main__":
    main()
    

