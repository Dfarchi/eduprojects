
from menus import menu_pick
import random


def first_class_fun(seat_class: str) -> dict:
    return {
        'class': seat_class,
        'line': random.randint(1, 5),
        'seat': random.choice(['A', 'B', 'C', 'D']),
        'meal': menu_pick('first'),
        'price': '$4000'
    }
