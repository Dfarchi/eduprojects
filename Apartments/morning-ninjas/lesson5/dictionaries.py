# friends = 7
# for i in range(friends):
#     print("fsfsd")
#     if i == 3:
#         i += 2

# key-value
my_dict = {
    123456789: "Valeria Aynbinder",
    987765234: "Ziv Attias",
    783465234: "Nehorai Tubul"
}
# print(my_dict[987765234])
# my_dict[333333333] = "Israel Israeli"
# print(my_dict)
#
# d1 = {
#     'Iphone 13': 5,
#     'Samsung Galaxy 22': 10,
#     'MacBook Pro': 8,
#     'a': 17
# }
# print(d1)
#
# d1['a'] = 20
# print(d1)
# d1['b'] = 222
#
# print(d1)

person1 = {
    'first_name': 'Valeria',
    'last_name': 'Aynbinder',
    'year': 1987,
    'id': 333333333,
    'phone': '0546666666'
}
person2 = {
    'first_name': 'Ziv',
    'last_name': 'Attias',
    'year': 1998,
    'id': 111111111,
    'phone': '0546664455'
}

# persons = [person1, person2]
# print(persons)
# for person in persons:
#     print(person['last_name'])

import pprint

persons_dict = {
    person1['id']: person1,
    person2['id']: person2
}
# pprint.pprint(persons_dict)

# my_list = [[123456789, "Valeria Aynbinder"],
#            [987765234, "Ziv Attias"],
#            [783465234, "Nehorai Tubul"]]
#
# for elem in my_list:
#     if elem[0] == 783465234:
#         print(elem[1])

# empty = {}
# empty = dict()
#
# empty_list = []
# empty_list = list()

# Implement a function insert_persons that receives int
# number n as argument, and asks the user to insert
# details of n persons. The details for each person include:
# id, first_name, last_name, year, phone.
# The function returns a dictionary with all the
# persons details

# def insert_persons(num: int) -> dict:
#     persons = {}

#     for i in range(num):
#         person = {}
#         person['id'] = input("Id: ")
#         person['first_name'] = input("f_name: ")
#         person['phone'] = input("Phone num: ")
#         #{}
#         #person['id'] = 2343343
#         #persons[2343343] = person
#         persons[person['id']] = person
#     return persons
#
# print(insert_persons(2))


# def insert_persons(num: int) -> dict:
#     persons = {}
#     fields = ('id', 'first_name', 'phone')
#     # fields(('id', int), ('first_nanme', str))
#     fields = {'id': int,
#               'first_name': str}
#     for i in range(num):
#         person = {}
#         for field in fields:
#             person[field] = input(f"Insert {field}: ")
#         persons[person['id']] = person
#     return persons
#
# print(insert_persons(2))
# representing an object

# using operator [] for read and assignment
grades = {
    'Ziv': [100, 100, 100],
    'Valeria': [89, 70],
    'Yael': [99, 98, 100]
}
grades['Noa'] = [100]
# grades[3] = True
# pprint.pprint(grades)
grades['Noa'].append(99)
# pprint.pprint(grades)


# iterating over dictionary
# for xxx in grades:
#     print(xxx)
#     print(grades[xxx])

# for xxx in grades.keys():
#     print(xxx)
#
# for xxx in grades.values():
#     print(xxx)

# for key, val in persons_dict.items():
#     print(key)
#     print(val)
#     if type(val) == dict:
#         for k, v in val.items():
#             print(f"k={k}")
#             print(f"v={v}")
#
# persons_dict = {
#     333333333: {
#         'first_name': 'Valeria',
#         'last_name': 'Aynbinder',
#         'year': 1987,
#         'id': 333333333,
#         'phone': '0546666666'
#     },
#     111111111: {
#         'first_name': 'Ziv',
#         'last_name': 'Attias',
#         'year': 1998,
#         'id': 111111111,
#         'phone': '0546664455'
#     }
# }
# for person_id, person_dict in persons_dict.items():
#     # if 'first_name' in person_dict:
#     #     print(person_dict['first_name'])
#     print(person_dict.get('first_name'))
#     print(person_dict['bbbb'])



# print(grades.keys())
# print(grades.values())
# dictionary methods

# for name, grades_list in grades.items():
#     print(f"{name}: {sum(grades_list) / len(grades_list)}")

# name = input("Insert name: ")
# print(f"{name}: {grades.get(name)}")
# print(f"{name}: {sum(grades.get(name, [])) / len(grades.get(name, []))}")
# print(grades)

# grades.pop('Ziv')
# del grades['Ziv']
# new_grades = {
#     'Yuval': [90, 95],
#     'Nehorai': [98, 97]
# }
# grades.update(new_grades)
# grades.update(new_grades)
# print(grades)


company_stocks_data = {
    'tsla': {
        'ticker': 'tsla',
        'company_name': 'Tesla',
        'employees_number': 5000,
        'address': 'Claifornia',
        'CEO_name': 'Elon Musk',
        'stocks data (per date)':{
            '14.11.2021':{
                'open price': 1001.5,
                'close price':1020,
                'volume': 50000000
            },
            '15.11.2021':{
                'open price': 1067.7,
                'close price':1045.5,
                'volume': 45000345
            }
        },
    },

    'apl': {
        'ticker': 'apl',
        'company name': 'Apple',
        'employees number': 10000,
        'address': 'New York',
        'CEO name': 'Tim Cook',
        'stocks data (per date)':{
            '14.11.2021':{
                'open price': 1001.5,
                'close price':1020,
                'volume': 50000000
            },
            '15.11.2021':{
                'open price': 1067.7,
                'close price':1045.5,
                'volume': 45000345
            }
        }


    }
}
pprint.pprint(company_stocks_data['tsla']['stocks data (per date)']['15.11.2021']['open price'])
# print(company_stocks_data['tsla']['stocks data (per date)']['15.11.2021'])
