def copy_and_replace(source_file, target_file):
    try:
        with open(source_file, 'r', encoding='utf-8') as src:
            content = src.read()
        
        updated_content = content.replace("cat", "dog")
 
        with open(target_file, 'w', encoding='utf-8') as dst:
            dst.write(updated_content)
            
        print(f"Успех: Содержимое '{source_file}' перенесено в '{target_file}' "
              f"с заменой 'cat' на 'dog'.")
              
    except FileNotFoundError:
        print(f"Ошибка: Файл '{source_file}' не найден. Убедитесь, что он существует.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

def main():
    src_file = "source.txt"
    dst_file = "destination.txt"
    
    print(f"--- Запуск процесса обработки файлов ---")
    copy_and_replace(src_file, dst_file)
    print("--- Работа завершена ---")

if __name__ == "__main__":
    main()
    
