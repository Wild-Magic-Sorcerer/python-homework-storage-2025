if __name__ == "__main__":
    is_even = lambda x: x % 2 == 0
    for i in range(1, 11):
        print(i, "→", is_even(i))
