text = input("Введите строку: ")
clean = text.replace(" ", "").lower()
if clean == clean[::-1]:
    print("Палиндром!")
else:
    print("Не палиндром(")
    n = len(clean)
    for i in range(n//2):
        if clean[i] != clean[n-(i+1)]:
            print(f"Символ {i} ({clean[i]}) ≠ символ {n - 1 - i} ({clean[n - 1 - i]})")
            break
