import unittest
from unittest import TestCase

from c3_2_exceptions import BankAccount


class AccountExc(TestCase):

    def test_create_account(self):
        with self.assertRaises(Exception):
            account = BankAccount("discount", 'bb', 123, set())

if __name__ == '__main__':
    unittest.main()