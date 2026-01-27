import argparse
if __name__ == '__main__':
    lines = argparse.ArgumentParser(description='Строки чисил')
    lines.add_argument('line', nargs='+')
    lines.add_argument('-f','--flag', type=bool, default=False)
    list_strok = lines.parse_args()

    if list_strok.flag:
        lines = list_strok.line
        print(len(lines))
    else:
        for i in list_strok.line:
            print(i)
