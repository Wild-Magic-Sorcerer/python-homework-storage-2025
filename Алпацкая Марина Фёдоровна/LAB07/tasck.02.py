import argparse

if __name__ == '__main__':
    numers = argparse.ArgumentParser(description='Числа и операции')
    numers.add_argument('x', type=float)
    numers.add_argument('y', type=float)
    numers.add_argument('-f', '--flag', type=str, default='none')
    procedure = numers.parse_args()

    if 'add' == procedure.flag.lower():
        result = procedure.x + procedure.y
    elif 'sub' == procedure.flag.lower():
        result = procedure.x - procedure.y
    elif 'mul' == procedure.flag.lower():
        result = procedure.x * procedure.y
    elif 'div' == procedure.flag.lower():
        result = procedure.x / procedure.y
    else:
        result = f'{procedure.x} и {procedure.y}'

    print(result)
