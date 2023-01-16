import pprint

from planeticket.first import first_class_fun
from planeticket.business import business_class_fun
from planeticket.economy import economy_class_fun

print("✈️ ✈️ ✈️ ")


def some_function(seat_class: str) -> dict:
    if seat_class == "first":
        return first_class_fun('first')
    elif seat_class == "business":
        return business_class_fun('business')
    elif seat_class == "economy":
        return economy_class_fun('economy')


# Greetings-------------------------------------------------------------------------------------------------------------


# Ask customer’s First name and Last name-------------------------------------------------------------------------------

print("please choose class first / business / economy")
seat_class = input("your seat's class is-")
seat_class = seat_class.lower()

while True:
    if seat_class == "first":
        print("----------✈✈✈----------")
        pprint.pprint(first_class_fun('first'))
        print("----------✈✈✈----------")

        break
    elif seat_class == "business":
        print("----------✈✈✈----------")
        pprint.pprint(business_class_fun('business'))
        print("----------✈✈✈----------")
        break
    elif seat_class == "economy":
        print("----------✈✈✈----------")
        print(economy_class_fun('economy'))
        print("----------✈✈✈----------")

        break
    else:
        seat_class = input("your seat's class could be first / business / economy champ").lower()

# discount fun----------------------------------------------------------------------------------------------------------


# useless dict:
# plane_seats_dict = {'first':{'lines_first':[1, 2, 3, 4,],'seats_first':['A', 'B', 'C', 'D']},
#                     'business':{'lines_business':[[5, 6, 7], [8, 9, 10]],'seats_business':['A', 'B', 'C', 'D']},
#                     'economy':{'lines_economy':[[11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
#                     [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
#                     [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]],
#                     'seats_economy':['A', 'B', 'C', 'D', 'E', 'F']}}
''
