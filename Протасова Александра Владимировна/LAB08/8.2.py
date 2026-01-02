def replace_dates_in_text(text):

    result = ""
    i = 0
    while i < len(text):
        if (i + 9 < len(text) and
                text[i:i + 2].isdigit() and
                text[i + 2] == '.' and
                text[i + 3:i + 5].isdigit() and
                text[i + 5] == '.' and
                text[i + 6:i + 10].isdigit()):

            if i == 0 or not text[i - 1].isdigit():
                if i + 10 == len(text) or not text[i + 10].isdigit():
                    result += "DD.MM.YYYY"
                    i += 10
                    continue
        result += text[i]
        i += 1
    return result

def main():
    text = input("Введите текст с датами: ")
    result = replace_dates_in_text(text)
    print("\nРезультат:")
    print(result)

if __name__ == "__main__":
    main()
