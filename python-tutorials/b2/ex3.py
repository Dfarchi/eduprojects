d = {
    'Science': [88, 89, 62, 95],
    'Language': [77, 78, 84, 80]
}

# [{'Science': 88, 'Language': 77},
# {'Science': 89, 'Language': 78},
# {'Science': 62, 'Language': 84},
# {'Science': 95, 'Language': 80}]


def dict2list(orig_dict) -> list:
    ret_list = []
    for prof, grades_list in orig_dict.items():
        for i, grade in enumerate(grades_list):
            if len(ret_list) < i+1:
                # this is the first iteration, so we need to create
                # an empty dictionary for each element we iterate
                ret_list.append({})
            ret_list[i][prof] = grade
    return ret_list


if __name__ == '__main__':
    print(dict2list(d))

# []
# [{}] -> [{'science': 92}]
# [{'science': 92}, {'science': 90},
#  {'science': 99}, {'science': 99}]
# [{'science': 92, 'lang':70}, {'science': 90, 'lang': 70},
#  {'science': 99, 'lang':70}, {'science': 99, 'lang':70}]
