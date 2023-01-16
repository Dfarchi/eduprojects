import system

class Nosuchtable(Exception):

    def __init__(self):
        super().__init__("there is no table with that Id in our restaurant")

class Notenoughseats(Exception):

    def __init__(self):
        super().__init__("there is not enough seats at this table")


class Allreadyavlble(Exception):

    def __init__(self):
        super().__init__("this table is not reserved yet")


