def main():
  words_input = input("Введите слова через пробел: ")
  # Создаем список слов, убирая лишние пробелы по краям
  words_list = words_input.split()
  
  # Сохраняем в кортеж
  words_tuple = tuple(words_list)
  print(f"Ваш кортеж: {words_tuple}")
  
  # Считаем уникальные слова
  unique_words = set(word.lower() for word in words_list)
  
  print(f"Количество уникальных слов: {len(unique_words)}")
  
if __name__ == "__main__":
      main()

