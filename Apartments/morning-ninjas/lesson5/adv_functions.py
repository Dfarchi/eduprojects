# mutable vs immutable arguments

# returning multiple values as tuple
# def analyze_str(word: str) -> tuple[int, str, str]:
#     return len(word), word.upper(), word.lower()


# ret_val = analyze_str('Hello')
# word_len, word_u, word_l = analyze_str('Hello')
# print(word_len, word_u, word_l)
# print(ret_val)
# a, b = (9,0)

# optional arguments (default values)
def create_person(person_id: int, name: str, address: str, phone=None, fax=None) -> dict:
    return {
        "id": person_id,
        "name": name,
        "address": address,
        "phone": phone,
        "fax": fax
    }

# print(create_person(234, name="Valeria", address="Netanya", fax="098845", phone="3845387563"))

# print(create_person(person_id=234, "Valeria", address="Netanya", fax="098845", phone="3845387563"))

# print(create_person(person_id=234, address="Netanya", fax="098845", phone="3845387563", name="Valeria"))

# *args
def a(*argv):
    print(f"type of argv: {type(argv)}, len: {len(argv)}")
    for arg in argv:
        print (arg)

# a('Hello', 'Welcome', 'to', 'Python', 'Class')

# def aa(argv:tuple):
#     print(f"type of argv: {type(argv)}, len: {len(argv)}")
#     for arg in argv:
#         print (arg)
#
# aa(('Hello', 'Welcome', 'to', 'Python', 'Class'))
# a()

# def a1(argv):
#     print(f"type of argv: {type(argv)}, len: {len(argv)}")
#     for arg in argv:
#         print (arg)

#a1(4,5)
#
# def b(person_id, name, *phone_numbers):
#     print ("First argument :", person_id)
#     print ("Second argument :", name)
#     for arg in phone_numbers:
#         print("Next argument through *phone_numbers :", arg)
#
# b(234, 'Valeria', '045-w4564', '045-srdfg', '0456456-dfg')

# b()

def c(**kwargs):
    print(type(kwargs))
    print(kwargs['first'])
    print(f"kwargs num: {len(kwargs)}, kwargs: {kwargs}")

def cc(person_id, name, **kwargs):
    print(person_id, name)
    print(kwargs)
#
# c(first='Python', mid ='Full', last='Stack')
# cc(345345, 'Valeria', work_address="tel aviv", age=40)
# c()
# c("Pyton")

# [3,4,1,2,6].sort(reverse=True)


def d(arg1, **kwargs):
    print(f"arg1: {arg1}")
    print(f"kwargs num: {len(kwargs)}, kwargs: {kwargs}")
#
# d(5, first="Hello", second="Bye")
# d(first=3)
# d(5, 'Hello')

#
#

# head, *tail = (1, 2,3,4)
#
# def d(person_id, name, *args, **kwargs):
#     print(person_id)
#     print(name)
#     print(f"args num: {len(args)}, args: {args}")
#     print(f"kwargs num: {len(kwargs)}, kwargs: {kwargs}")
# #
# d(5345, 'ziv', 'trrr', 56, first='abc', second='def')
# d()
# d(first='abc', 5)

# **kwargs

my_time = input("Insert time: ")
hours, minutes = my_time.split(':')
print(hours, minutes)
