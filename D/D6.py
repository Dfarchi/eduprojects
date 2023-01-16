import os
import csv
import json
from pprint import pprint

def d6_1(path: str, start: int, end: int):
    lines = ''
    if os.path.exists(path):
        with open(path, 'r') as f:
            if len(f.readlines()) >= end:
                f.seek(0)
                for line in f.readlines()[start - 1:end]:
                    lines += line
    return lines


def d6_2(path: str):
    if os.path.exists(path):
        with open(path, 'r') as f:
            reader = csv.reader(f)
            names = next(reader)
            cul_count = len(names)
            row_count = len(f.readlines())
            return names, cul_count, row_count + 1


#   with dictreader
def d6_21(path: str):
    if os.path.exists(path):
        with open(path, 'r') as f:
            file_obj = csv.DictReader(f)
            file_list = list(file_obj)
            names = file_list[0].keys()
            cul_count = len(names)
            row_count = len(file_list) + 1
            return names, cul_count, row_count


def d6_3(path: str, path2 : str):
    if os.path.exists(path):
        with open(path, 'r') as f:
            file_obj = list((csv.DictReader(f)))
            with open(path2, 'w') as j:
                json.dump(file_obj, j)
# (d6_3('.\\csv.csv','.\\json.json'))


def d6_4(path: str, path2: str):
    if os.path.exists(path):
        with open(path, 'r') as j:
            file_obj = json.load(j)
        with open(path2, 'w', newline='') as c:
            new_csv = csv.DictWriter(c, fieldnames=list(file_obj[0].keys()))
            new_csv.writeheader()
            new_csv.writerows(file_obj)

# d6_4('.\\json.json', '.\\csv2.csv')

# def d6_5(path: str):
#     ret_val = dict()
#     ret_val[f'{path}']= dict()
#     ret_val[f'{path}']['files'] = list()
#     for folder in os.listdir(path):
#         if '.' not in folder:
#             ret_val[f'{path}'][f'{folder}'] = []
#             for file in os.listdir(os.path.join(path,f'{folder}')):
#                 ret_val[f'{path}'][f'{folder}'].append(file)
#         else:
#             ret_val[f'{path}']['files'].append(folder)
#     return ret_val
# pprint(d6_5('C:\\Users\\user\\Desktop\\eduprojects\\D'))
# #
