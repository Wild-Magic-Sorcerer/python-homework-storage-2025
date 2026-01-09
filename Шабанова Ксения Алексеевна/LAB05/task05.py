def main():
    from datetime import datetime
    
    def logger(message, time=None):
        # Если время не передано, берем текущее
        if time is None:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Записываем в файл
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{time}] {message}\n")
    
    # Проверка работы
    msg = input("Введите сообщение для лога: ")
    logger(msg)
    
    print("Запись добавлена в log.txt")

if __name__ == "__main__":
    main()

