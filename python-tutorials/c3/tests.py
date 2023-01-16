from c3_2 import BankAccount


def test_conversion1():
    account = BankAccount('discount', 'rrr', 123, set(),
                          usd_allowed=True, credit_limit=0)
    account.deposit(100, 'nis')
    ret_val = account.convert_to_nis(1, 3.3)
    assert not ret_val, 'Allows to convert usd to nis when no usd in account'

def test_deposit():
    account = BankAccount('discount', 'rrr', 123, set(),
                          usd_allowed=True, credit_limit=0)
    ret_val = account.deposit(100, 'usd')
    assert ret_val, "Did not perform usd deposit"


if __name__ == '__main__':
    test_conversion1()
    test_deposit()