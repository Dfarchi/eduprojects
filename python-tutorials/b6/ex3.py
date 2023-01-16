import pprint

# # OPTION 0 - the easiest and not generic
# def insert_persons(num: int) -> dict:
#     ret_dict = {}
#     # id -> {id, name, phone}
#     for i in range(num):
#         person_id = input("id: ")
#         name = input("name: ")
#         phone = input("phone: ")
#
#         ret_dict[person_id] = {"id": person_id, "name": name, "phone": phone}
#     return ret_dict
#
# pprint.pprint(insert_persons(2))

# OPTION I
# def insert_persons(num: int) -> dict:
#     persons = {}
#     fields = ('id', 'first_name', 'phone')
#     for i in range(num):
#         person = {}
#         for field in fields:
#             person[field] = input(f"Insert {field}: ")
#         persons[person['id']] = person
#     return persons
#
# print(insert_persons(2))


# OPTION II
# def insert_persons(num: int) -> dict:
#     persons = {}
#     fields = {'id': "ID", 'first_name': "first name", 'phone': "phone number"}
#     for i in range(num):
#         person = {}
#         for field, user_friendly_str in fields.items():
#             person[field] = input(f"Insert {user_friendly_str}: ")
#         persons[person['id']] = person
#     return persons
#
# persons_num = int(input("Insert number of persons: "))
# pprint.pprint(insert_persons(persons_num))


# Option III with bonus
def insert_persons(n: int) -> dict:
    persons_dict = {}
    for i in range(n):

        person = {}
        fields_name = {'id': ['ID', int],
                       'name': ['name', str],
                       'birth_year': ['birth year', int],
                       'address': ['address', str]}
        for field, field_data in fields_name.items():
            value = input(f'Please enter {field_data[0]}: ')
            value_type = field_data[1]
            person[field] = value_type(value)

        persons_dict[person['id']] = person

    return persons_dict


pprint.pprint(insert_persons(2))


