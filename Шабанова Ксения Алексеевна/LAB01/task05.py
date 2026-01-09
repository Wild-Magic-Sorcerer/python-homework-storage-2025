def main():
  # Создаем исходный список от -10 до 10
  original_list = list(range(-10, 11))
  print(f"Исходный список: {original_list}")
  
  # Генератор списка: берем x, если x делится на 3 без остатка и x не ноль
  multiples_of_three = [x for x in original_list if x % 3 == 0 and x != 0]
  
  print(f"Числа, кратные 3: {multiples_of_three}")

if __name__ == "__main__":
    main()




