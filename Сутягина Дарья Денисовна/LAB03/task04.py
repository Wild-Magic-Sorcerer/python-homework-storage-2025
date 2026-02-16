def filters(**kwargs):
    vowels = "аеёиоуыэюяaeiou"
    result = {}

    for key, value in kwargs.items():
        if isinstance(value, str):
            count = sum(1 for ch in value.lower() if ch in vowels)
            if count >= 3:
                result[key] = value

    return result

def main():
    data = filters(name="Олег", city="Махачкала", test="привет")
    print("Результат:", data)

if __name__ == "__main__":
    main()
