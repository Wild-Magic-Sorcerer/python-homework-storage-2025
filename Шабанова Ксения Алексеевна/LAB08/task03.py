def main():
  import re
  
  text = input("Введите предложение: ")
  
  regex_pattern = r"[.,?! \-\n]+"
  
  # Разбиваем строку и убираем пустые элементы
  words = [w for w in re.split(regex_pattern, text) if w]
  
  
  print("Список слов:", words)

if __name__ == "__main__":
    main()

