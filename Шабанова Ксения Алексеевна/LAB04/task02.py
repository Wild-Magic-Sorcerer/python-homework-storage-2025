def main():
  fruits = ["apple", "banana", "cherry"]
  
  # Применяем len к каждой строке списка
  lengths = list(map(lambda s: len(s), fruits))
  
  print(f"Список строк: {fruits}")
  
  print(f"Длины строк: {lengths}")

if __name__ == "__main__":
    main()


