import sys

if __name__ == "__main__":

    if len(sys.argv) >= 2:
        username = sys.argv[1]
        print(f"Здравствуй {username}!")
    else:
        print("Please provide argument")

