import bank
import threading

# def open_account(password: str, name: str, address: str, clientid: str ):
#     new_account = bank.BankAccount(password, name, address, clientid)
#     return new_account

# this code should run without problems
if __name__ == '__main__':

    me = bank.Person('312427107', 'Yuval', 'Nofit', '0549982353')
    my_account = bank.BankAccount('123456', "Israel Israeli", 1, {me})

    t1 = threading.Thread(target=bank.multiple_transactions_deposit, args=(my_account,))
    t2 = threading.Thread(target=bank.multiple_transactions_deposit, args=(my_account,))
    t3 = threading.Thread(target=bank.multiple_transactions_withdraw, args=(my_account,))
    t4 = threading.Thread(target=bank.multiple_transactions_withdraw, args=(my_account,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    assert my_account.nis_balance == 0, \
       f"Expected balance: 0, received: {my_account.nis_balance}"
    assert len(my_account.transactions) == 799960, \
       f"Expected transactions: 799960, received: len(my_account.transactions_list)"
