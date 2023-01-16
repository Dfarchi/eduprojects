import unittest
from system import TableReservationSystem
from unittest import TestCase
import tables_tests
class TableTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # cls.table_1 = Table(table_id=1, seats=4)
        # cls.table_2 = Table(table_id=2, seats=4)
        # cls.table_3 = Table(table_id=3, seats=2)
        # cls.table_4 = Table(table_id=4, seats=2)
        # cls.table_5 = Table(table_id=5, seats=10)

        cls.table_sys = TableReservationSystem([4, 4, 2, 2, 10], 'EduLabs')

    def test_reserve(self):
        self.assertTrue(self.table_sys.reserve(4, 0))
        self.assertTrue(self.table_sys.reserve(3, 1))

        with self.assertRaises(tables_tests.Allreadyavlble):
            self.table_sys.reserve(1, 0)
            self.table_sys.reserve(5, 1)

        with self.assertRaises(tables_tests.Notenoughseats):
            self.table_sys.reserve(3, 2)
            self.table_sys.reserve(3, 3)

        with self.assertRaises(tables_tests.Nosuchtable):
            self.table_sys.reserve(1, 7)

    def test_release(self):
        self.table_sys.tables[1].occupied_seats = 3
        self.assertTrue(self.table_sys.release(1))

        with self.assertRaises(tables_tests.Allreadyavlble):
            self.table_sys.release(4)

        with self.assertRaises(tables_tests.Nosuchtable):
            self.table_sys.release(5)