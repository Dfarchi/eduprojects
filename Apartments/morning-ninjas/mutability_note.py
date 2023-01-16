# ['apple', 'pear', 'ananas'] => the same list, elems Upper
# ['apple', 'pear', 'ananas'] => new list, elem upper


def foo(my_list: list):
    for i, f in enumerate(my_list):
        my_list[i] = f.upper()


def foo2(my_list: list[str]) -> list:
    ret_val = []
    for f in my_list:
        ret_val.append(f.upper())
    return ret_val

# ['name', 'address', 'id'], [['valeria', 'netanya', 111], ['moshe']]
# [{'name':'valeria'...}, {'name': 'moshe'...}]
def foo3(fields: list[str], data: list[list]) -> list[dict]:
    ret_list = []
    for i in range(len(fields)):
        inner_dict = {}
        ret_list.append(inner_dict)

        # filling the dict
        # inner_dict = {'name':'valeria'...}
        # ret_list.append(inner_dict)
    return ret_list


if __name__ == "__main__":
    l1 = ['apple', 'pear', 'ananas']
    l2 = foo2(l1)
    print(l2)