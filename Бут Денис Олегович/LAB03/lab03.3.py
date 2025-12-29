def multiplying_args (*args):
    if not args:
        return None
    res_num = 1
    has_int = False
    for arg in args:
        if isinstance(arg, int) and not isinstance(arg, bool):
            res_num *= arg
            has_int = True

    return res_num if has_int else None

if __name__ == "__main__":
    list_for_def = [False,1,"ss",2,(1,4),4]
    print(multiplying_args(*list_for_def))
