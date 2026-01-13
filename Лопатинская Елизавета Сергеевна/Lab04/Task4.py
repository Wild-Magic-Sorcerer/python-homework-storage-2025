import random

def filter_numbers(data):
    return list(filter(lambda x: x > -5 and x % 2 == 0, data))

def main():
    original_list = random.sample(range(-20, 21), 20)
    filtered_list = filter_numbers(original_list)
  
    print(f"Исходный список:\n{original_list}\n")
    print(f"Отфильтрованный список ( > -5 и чётные):\n{filtered_list}")

if __name__ == "__main__":
    main()
  
