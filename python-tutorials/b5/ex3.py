c1 = ['red', 'white', 'blue', 'white', 'pink', 'purple', 'white']
c2 = ['red', 'White', 'BLUE', 'white & Red', 'sky blue', 'purple', 'orange with white straps']


def colors_intersection(colors1: list[str], colors2: list[str]) -> set[str]:
    return set([c.lower() for c in colors1]).intersection(set(c.lower() for c in colors2))


print(colors_intersection(c1, c2))