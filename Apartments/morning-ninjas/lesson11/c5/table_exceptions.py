class BaseTableException(Exception):
    pass

class TableAlreadyOccupied(BaseTableException):
    def __init__(self):
        super().__init__("Table already occupied")

class NotEnoughSeats(BaseTableException):
    def __init__(self):
        super().__init__("There is not enough seats at the table")

class TableNotFoundException(BaseTableException):
    def __init__(self):
        super().__init__("The table does not exist")