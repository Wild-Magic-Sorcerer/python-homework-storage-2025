def main():
  from functools import reduce
  
  numbers = list(range(1, 11))
  
  # Перемножаем элементы поочереди
  product = reduce(lambda x, y: x * y, numbers)
  
  print(f"Список: {numbers}")
  
  print(f"Произведение всех чисел: {product}")

if __name__ == "__main__":
    main()

