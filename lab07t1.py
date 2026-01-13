import argparse

def main():
    parser = argparse.ArgumentParser(description='Приветствие пользователя.')
    parser.add_argument('username', type=str, help='Имя пользователя для приветствия')
    args = parser.parse_args()
    print(f'Привет, {args.username}!')

if __name__ == '__main__':
    main()