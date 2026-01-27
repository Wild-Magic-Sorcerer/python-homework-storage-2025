import argparse
if __name__ == '__main__':
    user = argparse.ArgumentParser(description='Имя пользователя')
    user.add_argument('name', type=str)
    names = user.parse_args()
    if names.name: print(f'Приветствуем, {names.name}')
