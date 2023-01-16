# add locking mechanism and make thread-safe
from threading import Lock, Thread


class BankAccount:

    def __init__(self, account_num, holder_name):
        self._account_name = account_num
        self._holder_name = holder_name
        self._transactions_list = []  # just the name of the action
        self._balance = 0
        self._lock: Lock = Lock()

    @staticmethod
    def safe(f):
        def wrapper(self: "BankAccount", *args, **kwargs):
            with self._lock:
                return f(self, *args, **kwargs)

        return wrapper

    @safe
    def deposit(self, amount):
        self._balance += amount
        self._transactions_list.append("deposit")

    @safe
    def withdraw(self, amount):
        self._balance -= amount
        self._transactions_list.append("withdraw")


# this code should run without problems
if __name__ == '__main__':
    my_account = BankAccount(123456, "Israel Israeli")

    def multiple_transactions_deposit(account):
        for i in range(100, 2000000, 10):
            account.deposit(i)

    def multiple_transactions_withdraw(account):
        for i in range(100, 2000000, 10):
            account.withdraw(i)

    threads = [Thread(target=multiple_transactions_deposit, args=(my_account,)) for _ in range(4)]
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    assert my_account._balance == 0, \
        f"Expected balance: 0, received: {my_account._balance}"
    assert len(my_account._transactions_list) == 799960, \
        f"Expected transactions: 799960, received: {len(my_account._transactions_list)}"
