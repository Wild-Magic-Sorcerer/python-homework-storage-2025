Words = input()

def Tuple_and_Set(Words):
    Split_W = Words.split(" ")
    return tuple(Split_W), len(set(Split_W))


print(Tuple_and_Set(Words))
if __name__ == "__main__":
    ...