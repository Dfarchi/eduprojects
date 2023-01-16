various = ['AAA', [4, 5, 7], "5", 5,  3.0, True, 2654, -4, 0]
only_pos_ints = []

for elem in various:
    if type(elem) == int and int(elem) > 0:
        only_pos_ints.append(int(elem))

print(only_pos_ints)