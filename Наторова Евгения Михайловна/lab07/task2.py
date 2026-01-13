import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="приветствие")
    parser.add_argument("x", type=float, help="первое число")
    parser.add_argument("y", type=float, help="второе число")
    parser.add_argument("--operation", choices=['add','sub','mul','div'], help='операции')
    args = parser.parse_args()
    if args.operation == 'add':
        print(args.x + args.y)
    elif args.operation == 'sub':
        print(args.x - args.y)
    elif args.operation == 'mul':
        print(args.x * args.y)
    elif args.operation == 'div':
        print(args.x / args.y)
    else:
        print(args.x, args.y)
