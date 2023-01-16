def drop_empty(orig_dict: dict, inplace: bool = False):
    keys_to_remove = []
    for k, v in orig_dict.items():
        if not v:
            keys_to_remove.append(k)

    if inplace:
        # alter original dictionary
        for k in keys_to_remove:
            orig_dict.pop(k)

        return orig_dict

    else:
        # create a new dictionary
        new_dict = {}
        for k, v in orig_dict.items():
            if k not in keys_to_remove:
                new_dict[k] = v

        return new_dict

orig_dict = {
    'c1': 'Red',
    'c2': 'Green',
    'c3': None,
    'c4': [],
    'c5': ""
}

print(drop_empty(orig_dict, inplace=False))

