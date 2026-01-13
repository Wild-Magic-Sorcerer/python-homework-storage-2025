from functools import reduce

if __name__ == "__main__":
    nums = list(range(1, 11))
    product = reduce(lambda x, y: x * y, nums)

    print(f"произведение всех элементов {nums} = {product}")
    

