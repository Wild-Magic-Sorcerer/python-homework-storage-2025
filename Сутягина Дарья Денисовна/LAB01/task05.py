import random

if __name__ == "__main__":
    nums = [random.randint(-10, 10) for i in range(20)]  # 20 чисел в диапазоне
    numb3 = [x for x in nums if x % 3 == 0]

    print(nums)
    print(numb3)
    
