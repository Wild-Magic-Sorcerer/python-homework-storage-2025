import random
if __name__ == "__main__":
        nums = [random.randint(-20, 20) for i in range(10)]

        filter_nums = list(filter(lambda x: x > -5 and x % 2 == 0, nums))


        print(f"начальный список {nums}, отфильтрованный список {filter_nums}")
        
