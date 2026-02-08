import re

def replace_dates_in_text(text1):
    pattern = r'\b\d{2}\.\d{2}\.\d{4}\b'
    result1 = re.sub(pattern, 'DD.MM.YYYY', text1)
    return result1

def get_input_text():
    return input("Введите текст с датами: ")

if __name__ == "__main__":
    text = get_input_text()
    result = replace_dates_in_text(text)
    print("\nРезультат:")
    print(result)
