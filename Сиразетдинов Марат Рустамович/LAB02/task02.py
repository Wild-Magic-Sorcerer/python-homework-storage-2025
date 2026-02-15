def analyze_string(text):
    text = text.strip()

    if not text:

        return {'words': 0, 'letters': 0, 'digits': 0, 'spaces': 0, 'punctuation': 0}

    words = len(text.split())

    letters = digits = spaces = punctuation = 0

    for char in text:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        else:
            punctuation += 1

    return {
        'words': words,
        'letters': letters,
        'digits': digits,
        'spaces': spaces,
        'punctuation': punctuation
    }
