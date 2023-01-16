import random

from menus import menu_pick
from utils import yes_or_no


def business_class_fun(seat_class: str) -> dict:
    receipt = {
        'class': seat_class,
        'price': 0
    }

    print("choose line: Lines 5-7 => price $3000 Lines 8-10 => price $2300")
    line = (input("your line-"))
    while True:
        if line.isnumeric():
            line = int()
            break
        else:
            line = input("must be a number between 5-10")
    while True:
        if 7 >= line >= 5:
            receipt['line'] = line
            receipt['price'] += 3000
            break
        elif 10 >= line >= 8:
            receipt['line'] = line
            receipt['price'] += 2300
            break
        else:
            line = (int(input("business lines are between 5-10, plz choose again-")))

    seat = yes_or_no(input("would you like window seat? its a 55$ fee-").lower())
    if seat == 'yes':
        seats = ['A', 'D']
        random.shuffle(seats)
        receipt['seat'] = seats[0]
        receipt['price'] += 55
    elif seat == 'no':
        seats = ['C', 'B']
        random.shuffle(seats)
        receipt['seat'] = seats[0]
        receipt['seat'] = seat

    meal = yes_or_no(input("would you like a first class meal?(+ $42)").lower())
    if meal == 'yes':
        receipt['meal'] = menu_pick('first')
        receipt['price'] += 42
    else:
        receipt['meal'] = menu_pick('business')

    luggage = yes_or_no(input("would you like to bring luggage that exceeds 50kg?(+ $10)").lower())
    if luggage == 'yes':
        receipt['price'] += 42
        receipt['luggage'] = 'endless'
    return receipt
