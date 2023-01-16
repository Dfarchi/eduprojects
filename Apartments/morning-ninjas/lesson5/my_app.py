from validators import *


def print_greeting(name):
    print("Hello", name)


print("__name__ of",__file__, __name__)

if __name__ == '__main__':
    print_greeting(input("name: "))
    num = insert_int()
    print(num)
    print("bye")