class BankAccountException(Exception):
    pass

# class InvalidParamError(BankAccountException):
#     pass
#
# class InsufficientFundsError(BankAccountException):
#     pass

class InvalidParamError(BankAccountException):
    MSG = "Invalid param received"

    def __init__(self):
        super().__init__(self.MSG)


class InsufficientFundsError(BankAccountException):
    def __init__(self):
        super().__init__("Insufficient funds")