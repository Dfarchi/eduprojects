# Write a function that receives a sequence of key-value pairs and creates
# a dictionary of lists (and returns it). For example:
# Original list:
# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}


def make_dict(orig_list: list[tuple[str, int]]) -> dict[str, list[int]]:
    ret_dict: dict[str:list[int]] = {}

    for orig_key, orig_num in orig_list:
        if orig_key not in ret_dict:
            ret_dict[orig_key] = []
        ret_dict[orig_key].append(orig_num)
    return ret_dict
