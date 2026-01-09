def main():
  import re
  
  input_str = input("Введите текст с датами: ")
  
  # Ищем шаблон ДД.ММ.ГГГГ 
  date_pattern = r"\d{2}\.\d{2}\.\d{4}"
  
  # Заменяем все вхождения на DD.MM.YYYY
  result = re.sub(date_pattern, "DD.MM.YYYY", input_str)
  
  
  print("Результат:", result)

if __name__ == "__main__":
    main()


