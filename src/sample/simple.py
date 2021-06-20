import sys

def add_one(number):
    return number + 1


def add_two(number):
    return number + 2

def entrypoint():
    print(add_two(int(sys.argv[1])))