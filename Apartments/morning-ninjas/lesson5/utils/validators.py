TIME_SEPARATOR = ':'

def insert_int():
    while True:
        num = input("Insert a num: ")
        if num.isdigit():
            return int(num)


def insert():
    return input("Insert something: ")

