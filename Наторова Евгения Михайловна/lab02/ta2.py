def analyz(text):
    text = text.strip()
    stati = {'words': 0,'letters': 0, 'digits': 0, 'spaces': 0, 'punct': 0}

    stati['words'] = len([word for word in text.split() if word])

    for char in text:
        if char.isalpha():
            stati['letters'] += 1
        elif char.isdigit():
            stati['digits'] += 1
        elif char.isspace():
            stati['spaces'] += 1
        elif char in '.,;:!?-"\'()[]{}':
            stati['punct'] += 1

    return stati

if __name__ == "__main__":
    text = input("введите строку для анализа: ")
    result = analyz(text)
    print(f"cлов: {result['words']},"
          f" букв: {result['letters']},"
          f" цифр: {result['digits']},"
          f" пробелов: {result['spaces']},"

          f" знаков препинания: {result['punct']} ")
    
