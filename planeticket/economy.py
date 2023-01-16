import random

from utils import yes_or_no
from menus import menu_pick


def economy_class_fun(seat_class: str) -> dict:
    receipt = dict()
    receipt['class'] = seat_class
    receipt['price'] = 0
    # Lines: 12,22,42 for extra fee ( + $15)
    print("choose line: Lines 11-20 => price $1700 Lines 21-40 => price $1500 Lines 41-60 => price $1200")
    line = (input("your line-"))
    while True:
        if line.isnumeric():
            line = int()
            break
        else:
            line = input("must be a number between 11-60")
    while True:
        if 20 >= line >= 11:
            receipt['line'] = line
            receipt['price'] += 1700
            break
        elif 40 >= line >= 21:
            receipt['line'] = line
            receipt['price'] += 1500
            break
        elif 60 >= line >= 41:
            receipt['line'] = line
            receipt['price'] += 1200
            break
        else:
            line = (int(input("economy lines are between 11-60, plz choose again-")))

    seat = yes_or_no(input("would you like window seat? its a 55$ fee-").lower())
    if seat == 'yes':
        seats = ['A', 'F']
        random.shuffle(seats)
        receipt['seat'] = seats[0]
        receipt['price'] += 55
    elif seat == 'no':
        seats = ['B', 'C', 'D', 'E']
        random.shuffle(seats)
        receipt['seat'] = seats[0]

    meal = (input("would you like a first class meal(+ $42) a business meal (+$7) or an economy meal?").lower())
    while True:
        if meal == 'first':
            receipt['meal'] = menu_pick('first')
            receipt['price'] += 42
            break
        elif meal == 'business':
            receipt['meal'] = menu_pick('business')
            receipt['price'] += 7
            break
        elif meal == 'economy':
            receipt['meal'] = 'economy meal'
            break
        else:
            meal = input("'first', 'business' or 'economy' -")

    luggage = yes_or_no(input("would you like to bring luggage that exceeds 20kg?(+ $10)").lower())
    if luggage == 'yes':
        receipt['price'] += 10
        receipt['luggage'] = 'up to 50kg'
    return receipt
