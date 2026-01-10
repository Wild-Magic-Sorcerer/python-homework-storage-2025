import random

def main():
  
  # Создаем произвольный список (я взяла random для интереса)
  my_list = [random.randint(-20, 20) for _ in range(15)]
  
  # Фильтруем
  filtered_list = list(filter(lambda x: x > -5 and x % 2 == 0, my_list))
  
  print(f"Исходный список: {my_list}")
  
  print(f"Отфильтрованный список: {filtered_list}")

if __name__ == "__main__":
    main()



