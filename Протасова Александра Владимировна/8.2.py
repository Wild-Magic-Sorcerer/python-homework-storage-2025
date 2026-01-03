import re

def replace_dates_in_text(text):

    pattern = r'\b\d{2}\.\d{2}\.\d{4}\b'

    result = re.sub(pattern, 'DD.MM.YYYY', text)

    return result

def main():
    text = input("Введите текст с датами: ")
    result = replace_dates_in_text(text)
    print("\nРезультат:")
    print(result)

if __name__ == "__main__":
    main()
