colors_2 = ['red', 'White', 'BLUE','white', 'Red', 'sky blue', 'purple', 'orange with white straps']


def unique_colors(colors: list[str]) -> set:
    ret_val = set()
    for color in colors:
        ret_val.add(color.lower())
    return ret_val


# def unique_colors(colors: list[str], num: int ) -> set:
#     for i, c in enumerate(colors):
#         colors[i] = c.lower()

