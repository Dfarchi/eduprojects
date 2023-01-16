# from clientel import *
# from numbergenerator import *
# from converter import *
# import random
# from datetime import date
#
# # hey
#
#
# class Bank:
#     def __init__(self, password: str, name: str, address: str, clientid: str):
#         self.accountid = {}
#         client = Client(password, name, address, clientid)
#         self.accountid[clientid] = client
#         self.account = {'client': client,
#                         'account number': card_generator(),
#                         'branch number': ''.join(map(str, [random.randint(0, 9) for _ in range(0, 3)])),
#                         'balance': 0,
#                         'limits': [0, 1000],
#                         'currency': 'Nis',
#                         'transactions': {'date': []},
#                         }
#
#     def __repr__(self):
#         return str(self.account)
#
#     def __str__(self):
#         return str(self.account)
#
#     def withdrawal(self, password: str, amn: float):
#         if self.account['client'].password == password:
#             if self.account['limits'][0] < self.account['balance']:
#                 self.account['balance'] -= amn
#                 self.account['transactions'].update(str(date) + '-'+str(amn) + self.account['currency'])
#                 return print("new balance for", self.account['client'].name, self.account['balance'])
#             else:
#                 print("insufficient funds")
#                 return False
#         else:
#             return False
#
#     def deposit(self, password: str, amn: float,):
#         if password == self.account['client'].password:
#             if self.account['limits'][0] <= self.account['balance']:
#                 self.account['balance'] += amn
#                 self.account['transactions'].update(str(date) + '+'+str(amn) + self.account['currency'])
#                 print("new balance for", self.account['client'].name, self.account['balance'])
#                 if self.account['limits'][1] <= self.account['balance']:
#                     print("you've now deposited over the amount of your credit limits, plz contact us soon")
#             return True
#         else:
#             print("wrong password")
#             return False
#
#     def account_limit(self, min_limit, max_limit):
#         self.account['limits'][0] = min_limit
#         self.account['limits'][1] = max_limit
#
#     def transfer(self, amn, client1_password: str, client2_id: str, client2_password: str):
#         if client1_password == self.account['client'].password:
#             self.withdrawal(client1_password, amn)
#             # client2 = self.account[client2_id]
#             self.account[client2_password].bank.deposit(client2_password, amn)
#
#         else:
#             return False
#
#
#     # def converter_to_usd(self, amnt):
#     #     currency = self.account['currency']
#     #     converter.USDConverter.convert_to_usd(currency, amnt)
#     #     pass
################################################################

import datetime

from typing import Set, List, Tuple


class Person:

    def __init__(self, person_id: str, name: str, address: str, phone: str):
        self.id = person_id
        self.name = name
        self.address = address
        self.phone = phone


class Transaction:

    def __init__(self, amount: float, currency: str, ts: datetime.datetime):
        self.amount = amount
        self.currency = currency
        self.ts = ts
    def __repr__(self):
        return f"{self.__class__.__name__} - {self.amount} - {self.currency}. {self.ts}"

    def __str__(self):
        return self.__repr__()

class Deposit(Transaction):

    pass

class Withdrawal(Transaction):
    pass

class Conversion(Transaction):

    def __init__(self, amount: float, currency: str, ts, rate):
        super().__init__(amount, currency, ts)
        self.date = datetime.date
        self.rate = rate

    def __repr__(self):
        return f"{super().__repr__()} , rate:{self.rate}"


class BankAccount:

    def __init__(self, bank_name: str, branch: str, account_num: int, holders: Set[Person],
                 usd_allowed: bool = False, credit_limit: float = 0):
        self.bank_name: str = bank_name
        self.branch: str = branch
        self.account_num: int = account_num
        self.holders: Set[Person] = holders

        self.nis_balance: float = 0
        self.usd_balance: float = 0
        self.usd_allowed: bool = usd_allowed
        self.nis_credit_limit: float = credit_limit

        self.transactions: dict[datetime.date:List[Transaction]] = {}

    def __str__(self):
        return f"Account {self.account_num}"

    @staticmethod
    def _valid_params(amnt, currency):
        return amnt > 0 and currency in ('nis', 'usd')

    def _add_transaction(self, amount: float, currency: str):
        transaction_date = datetime.date.today()

        # add new dictionary key if needed
        if transaction_date not in self.transactions:
            self.transactions[transaction_date] = []

        # if we are here, we are sure that the key already exists
        self.transactions[transaction_date].append(
            Transaction(amount, currency, ts)
        )

    def withdraw(self, amount: float, currency: str = 'nis') -> bool:

        if not self._valid_params(amount, currency):
            return False

        if currency == 'nis':
            if self.nis_balance - amount >= (self.nis_credit_limit * -1):
                self.nis_balance -= amount
            else:
                return False
        else:
            if self.usd_allowed and self.usd_balance >= amount:
                self.usd_balance -= amount
            else:
                return False
        self._add_transaction(amount=amount, currency=currency)
        return True

    def deposit(self, amount: float, currency: str = 'nis'):
        if not self._valid_params(amount, currency):
            return False

        if currency == 'nis':
            self.nis_balance += amount
            self._add_transaction(amount=amount, currency=currency)
            return True
        else:
            if not self.usd_allowed:
                return False
            else:
                self._add_transaction(amount=amount, currency=currency)
                self.usd_balance += amount

    def convert_to_usd(self, nis_amnt):
        if nis_amnt < 0:
            return False
        if not self.usd_allowed or self.nis_balance - nis_amnt < (self.nis_credit_limit * -1):
            return False
        self.nis_balance -= nis_amnt
        self.usd_balance += nis_amnt * Conversion.rate
        self._add_transaction(amount=nis_amnt, currency='nis')
        return True

    def convert_to_nis(self, usd_amnt, utn:Conversion):
        if usd_amnt < 0:
            return False
        if not self.usd_allowed or self.usd_balance < usd_amnt:
            return False
        self.nis_balance += usd_amnt * utn.usd2nis_exchange_rate
        self.usd_balance -= usd_amnt
        self._add_transaction(amount=usd_amnt, currency='usd')
        return True

    def get_current_balance(self) -> Tuple[float, float]:
        return self.nis_balance, self.usd_balance

    def get_transactions_per_date(self, date: datetime.date) -> List[Transaction]:
        return self.transactions.get(date, [])

def multiple_transactions_deposit(account):
    for i in range(100, 2000000, 10):
        account.deposit(i)

def multiple_transactions_withdraw(account):
    for i in range(100, 2000000, 10):
        account.withdraw(i)

    # create bank account

#
# account1 = BankAccount('Discount', 'Kiryat Hasharon', 12345,
#                        {Person('123456789', 'Valeria', 'Netanya', '054-444-4444')},
#                        usd_allowed=True, credit_limit=10_000)
# print(f"Current balance for {account1}: {account1.get_current_balance()}")
#
# print("Trying to withdraw 10500 shekels passing the limit - should fail!")
# result = account1.withdraw(10500)
# print(f"Result: {result}")
#
# print("Trying to withdraw 9500 shekels in the range of limit - should succeed!")
# result = account1.withdraw(9500)
# print(f"Result: {result}")
#
# print(f"Current balance: {account1.get_current_balance()}")
#
# print("Trying to convert 1000 shekels to USD - outside the limit, should fail")
# result = account1.convert_to_usd(1000, 3.5)
# print(f"Result: {result}")
#
# print("Deposit 20_000 to account - should succeed")
# result = account1.deposit(20000)
# print(f"Result: {result}")
#
# print("Deposit $5_000 to account - should succeed")
# result = account1.deposit(5000, currency='usd')
# print(f"Result: {result}")
#
# print(f"New balance: {account1.get_current_balance()}")
# print(f"Transactions: {account1.get_transactions_per_date(datetime.date.today())}")