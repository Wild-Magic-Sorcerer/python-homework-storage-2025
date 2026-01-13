import argparse

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("strings", nargs='+', help="Список строк")
    parser.add_argument("--count", action="store_true", help="Посчитать количество")
    
    args = parser.parse_args()
    
    if args.count:
        print(f"Количество строк: {len(args.strings)}")
    else:
        for s in args.strings:
    
            print(s)
            
if __name__ == "__main__":
    main()
    

