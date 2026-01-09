def main():
  date_str = input("Введите дату и время (ДД.ММ.ГГГГ ЧЧ:ММ:СС): ")
  
  # Сначала разделим на дату и время по пробелу
  parts = date_str.split()
  date_part = parts[0]
  time_part = parts[1]
  
  # Теперь "режем" дату по точкам, а время по двоеточиям
  day, month, year = date_part.split(".")
  hours, minutes, seconds = time_part.split(":")
  
  print(f"День: {day}")
  print(f"Месяц: {month}")
  print(f"Год: {year}")
  print(f"Часы: {hours}")
  print(f"Минуты: {minutes}")
  
  print(f"Секунды: {seconds}")

if __name__ == "__main__":
    main()

