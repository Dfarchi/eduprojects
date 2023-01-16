import unittest
from unittest import TestCase

from c3_2 import BankAccount


class DepositTests(TestCase):


    def setUp(self) -> None:
        self.account = BankAccount('discount', 'rrr', 123, set(),
                              usd_allowed=True, credit_limit=0)

    def test_nis_deposit(self):
        ret_val = self.account.deposit(100, 'nis')
        self.assertTrue(ret_val, msg="cannot deposit nis")

    def test_usd_deposit_when_allowed(self):
        account = BankAccount('discount', 'rrr', 123, set(),
                              usd_allowed=True, credit_limit=0)
        self.assertTrue(account.deposit(100, 'usd'), msg='did not deposit usd')

    def test_usd_deposit_when_not_allowed(self):
        pass

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    deposit_test_case = DepositTests()
    deposit_test_case.run()