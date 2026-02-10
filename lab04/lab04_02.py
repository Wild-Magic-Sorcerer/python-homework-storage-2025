# Дан список строк: ["apple", "banana", "cherry"]
# Используя функцию map и лямбда-функцию, получите новый список, состоящий из длин каждой строки

fruits_and_berries = ["apple", "banana", "cherry"]
if __name__ == '__main__':
    l = lambda x: len(x)
    fnb_numbers = list(map(l, fruits_and_berries))
    print(list(fnb_numbers))
    
