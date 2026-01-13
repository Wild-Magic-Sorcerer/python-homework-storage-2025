import string
def analyze_string(input_string):

    cleaned_string = input_string.strip()

    words = cleaned_string.split()

    word_count = len(words)
    letter_count = sum(c.isalpha() for c in cleaned_string)
    digit_count = sum(c.isdigit() for c in cleaned_string)
    space_count = cleaned_string.count(' ')
    punctuation_count = sum(c in string.punctuation for c in cleaned_string)

    result = {
        'words': word_count,
        'letters': letter_count,
        'digits': digit_count,
        'spaces': space_count,
        'punctuation': punctuation_count
    }
    return result


input_string = " Привет, мир! Как дела?  "
result = analyze_string(input_string)
print(result)