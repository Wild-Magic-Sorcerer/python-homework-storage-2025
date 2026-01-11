if __name__ == "__main__":
    from functools import reduce

    nums = list(range(1, 11))
    product = reduce(lambda x, y: x * y, nums)

    print(f"произведение всех элементов {nums} = {product}")
    
