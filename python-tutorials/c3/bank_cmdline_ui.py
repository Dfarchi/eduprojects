from bank_account_exceptions import BankAccountException, InvalidParamError, InsufficientFundsError
from c3_2_exceptions import BankAccount, Person
import threading

if __name__ == '__main__':
    # nmae = input("insert name")
    my_account = BankAccount('discount', 'ddd', 123,
                             {Person(1234, 'val', 'netanya', '046374653')})


    # while True:
    #     try:
    #         amnt = int(input("Inesrt amount to withdraw: "))
    #         crncy = input("Inesrt currency to withdraw: ")
    #         bank_account.withdraw(amnt, crncy)
    #         print("Operation succeded")
    #         break
    #     except ValueError:
    #         print("you inserted invalid amount")
    #     except BankAccountException as e:
    #         print(e)
    # # except InvalidParamError:
    # #     print("params")
    # # except InsufficientFundsError:
    # #     print("funds")
    # this code should run without problems
    # if __name__ == '__main__':
    #     my_account = BankAccount(123456, "Israel Israeli")
    #


    def multiple_transactions_deposit(account):
        for i in range(100, 2000000, 10):
            account.deposit(i)


    def multiple_transactions_withdraw(account):
        for i in range(100, 2000000, 10):
            account.withdraw(i)


    t1 = threading.Thread(target=multiple_transactions_deposit, args=(my_account,))
    t2 = threading.Thread(target=multiple_transactions_deposit, args=(my_account,))
    t3 = threading.Thread(target=multiple_transactions_withdraw, args=(my_account,))
    t4 = threading.Thread(target=multiple_transactions_withdraw, args=(my_account,))

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

    [transactions_list.append(t) for t in list(my_account.transactions.values())]
    transactions_total = len
    assert len(my_account.transactions.values) == 799960, \
        f"Expected transactions: 799960, received: {len(my_account.transactions.values)}"
