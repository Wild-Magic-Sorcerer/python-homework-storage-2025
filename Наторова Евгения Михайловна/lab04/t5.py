if __name__ == "__main__":
    import datetime

    def decor(func):

        def wrapper(*args, **kwargs):
            print("выполняется функция...")
            result = func(*args, **kwargs)
            print("функция выполнена.")
            return result

        return wrapper

    @decor
    def nowtime():
        return datetime.datetime.now()

    itime = nowtime()
    print(f"время {itime}")
    
