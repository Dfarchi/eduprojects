import random
import pprint
from utils import yes_or_no


def menu_pick(seat_class: 'str') -> str:
    menus = {
        'Menu1': {'STARTER': 'Roast veal sweetbread', 'MAIN': 'Cornish turbot', 'DESERT': 'Hazelnut souffle'},
        'Menu2': {'STARTER': 'Ravioli lobster', 'MAIN': '100-Day aged Cumbrian Blue Grey', 'DESERT': 'Pecan praline'},
        'Menu3': {'STARTER': 'Scallops from the Isle of Skye', 'MAIN': 'Aynhoe Park fallow deer',
                  'DESERT': 'Caramelised apple Tarte Tatin'}
    }
    if seat_class == 'first':
        print("would you like to pick a menu or let us choose for you?")
        meal = yes_or_no((str(input("yes - pick yourself, no - we pick for you"))))
        if meal == 'yes':
            print("🍤🍤🍤we got gordon FUCKIN ramzy on daplane!🍤🍤🍤")
            print("now please, choose a menu:")
            for menu_num, course in menus.items():
                print(f'[ {menu_num} ]')
                for course_type, meal in course.items():
                    print(f'\tFor {course_type}: {meal}')

            print("please pick a menu by typing 1 / 2 / 3")
            menu = input("your choice is -")
            while menu not in "123":
                menu = input("your choice has to be 1 / 2 / 3")
            else:
                return menus[f'Menu{menu}']
        if meal == 'no':
            return random.choice(list(menus.values()))
    elif seat_class == 'business':
        return random.choice(list(menus.values()))
