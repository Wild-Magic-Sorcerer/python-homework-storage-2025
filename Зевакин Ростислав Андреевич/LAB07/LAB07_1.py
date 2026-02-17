import sys

username = sys.argv[1] if len(sys.argv) > 1 else None
print(f"Доброго времени суток, {username}")
