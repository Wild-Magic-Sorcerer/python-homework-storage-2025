import argparse

def main():
  
  parser = argparse.ArgumentParser(description="Приветствие пользователя")
  parser.add_argument("name", help="Имя пользователя")
  
  args = parser.parse_args()
  
  
  print(f"Привет, {args.name}!")

if __name__ == "__main__":
    main()


