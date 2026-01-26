def multiplying_args(*args):
    if not args:
        return None
    res_num = 1
    list_of_arg = [res_num := res_num*arg for arg in args if isinstance(arg, int) and not isinstance(arg, bool)]
    return res_num, list_of_arg

if __name__ == "__main__":
    list_for_def = [False,1,"ss",2,(1,4),4]
    print(multiplying_args(*list_for_def))



