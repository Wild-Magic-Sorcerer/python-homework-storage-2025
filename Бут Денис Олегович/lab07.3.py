import sys

def counter_of_str (some_list):
    if not some_list:
        return None
    if some_list[-1] in ["-c","--count"]:
        return len(some_list[1:-1])
    return " ".join(some_list[1:])

if __name__ == "__main__":
    print(counter_of_str(sys.argv))