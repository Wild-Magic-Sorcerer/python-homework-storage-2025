def main():
    # заданный список (константа)
    NUMBERS_LIST = [1, 2, 3, 2, 1, 4, 2, 5, 1, 1, 3]
    
    count_dict = {}
    
    for num in NUMBERS_LIST:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    print("Результаты подсчета:")
    for number, count in count_dict.items():
    
        print(f"{number} — {count}")
    
if __name__ == "__main__":
    main()




