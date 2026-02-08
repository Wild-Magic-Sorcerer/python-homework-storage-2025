import time

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Выполняется функция...")
        result = func(*args, **kwargs)
        print("Функция выполнена.")
        return result
    return wrapper

@decorator
def current_time():
    return time.strftime("%H:%M:%S")

if __name__ == "__main__":
    time = current_time()
    print("Текущее время:", time)