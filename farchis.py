import time

class Table:
    def __init__(self, time_limit: int, seats: int, num: str):
        self.num = num
        self.availability = True
        self.beginning = time.time()
        self.seats = seats
        self.used_seats = 0
        self.time_left = (time_limit - (time.time() - self.beginning))

    def __repr__(self):
        return f'Table {self.num}'

    def __lt__(self, other):
        return self.seats > other.seats

    def release_table(self):
        self.availability = True
        self.used_seats = 0


class Floor:
    def __init__(self, name):
        self.restaurant_name = name
        self.tables = {'floor': [Table(90, 6, '1'), Table(90, 6, '2'), Table(90, 6, '3'), Table(90, 6, '4')],
                       'bar': [Table(90, 2, '100'), Table(90, 2, '102'), Table(90, 2, '104'), Table(90, 2, '106')],
                       'garden': [Table(120, 8, '11'), Table(120, 8, '12'), Table(120, 8, '13')]}

    def __repr__(self):
        return f'{self.restaurant_name}'

    def location(self, cus):
        if cus <= 2:
            return 'bar'
        elif 2 < cus <= 6 and not cus == 4:
            return 'floor'
        elif 6 < cus <= 8 or cus == 4:
            return 'garden'

    def get_available_tables(self, cus=0):
        if not cus:
            availablelist = []
            for l in self.tables.values():
                for t in l:
                    if t.availability == True:
                        availablelist.append(t)
            return print(f"available_tables are {availablelist}")
        else:
            available_tables = [t for t in self.tables[self.location(cus)] if t.availability]
            available_seats = [t for t in available_tables if t.seats >= cus]
            # print(f"available_seats in {self.location(cus)} are{available_seats}")
            if len(available_seats) == 0:
                print('no free tables')
                return False
            return sorted(available_seats)[-1]

    def next_available_table(self, cus=0):
        notavailablelist = []
        for l in self.tables.values():
            for t in l:
                if t.availability == False:
                    notavailablelist.append(t)
        if not cus:
            nextable = min(table.time_left for table in notavailablelist)
            for table in notavailablelist:
                if table.time_left == nextable:
                    return table, table.time_left
        else:
            next_big_enough = min([table.time_left for table in notavailablelist if table.seats >= cus])
            for table in notavailablelist:
                if table.time_left == next_big_enough:
                    return table, table.time_left

    def get_reserved_tables(self, time=0):
        notavailablelist = []
        for l in self.tables.values():
            for t in l:
                if t.availability == False:
                    notavailablelist.append(t)
        if not time:
            for t in notavailablelist:
                print(f"{t} would be free in {t.time_left} minutes")
        if time:
            for t in notavailablelist:
                    if t.time_left <= time:
                        print(f"{t} would be free in {t.time_left} minutes")


    def get_customers(self):
        customers = 0
        for l in self.tables.values():
            for t in l:
                customers += t.used_seats
            return print(customers, ' seated customers ')

    def get_capacity(self):
        capacity = 0
        for l in self.tables.values():
            for t in l:
                capacity += t.seats
            return print(capacity, 'max capacity')

    def reserve_table(self, cus: int):
        if self.get_available_tables(cus):
            t = self.get_available_tables(cus)
            t.availability = False
            t.used_seats = cus
            return t
        else:
            print("no available tables for that amount of people")
            return False

    def status(self):
        for l in self.tables.values():
            for t in l:
                print(t, f" {t.used_seats}/{t.seats} taken seats , time left is {t.time_left} minutes")





farchis = Floor('farchis')
farchis.get_capacity()
a = farchis.reserve_table(3)
b = farchis.reserve_table(7)
c = farchis.reserve_table(7)
d = farchis.reserve_table(7)
ab = farchis.reserve_table(7)
# farchis.get_customers()
# print(farchis)
# # print(a, f"seats {a.seats}, taken {a.used_seats}, time left {a.time_left} minutes")
# # a.release_table()
# # print(a.availability)
# # print(farchis.tables.values())
# print(a, f" {a.used_seats}/{a.seats} taken seats , time left is {a.time_left} minutes{a.availability}")
# print(b, f" {b.used_seats}/{b.seats} taken seats , time left is {b.time_left} minutes")
# print(c, f" {c.used_seats}/{c.seats} taken seats , time left is {c.time_left} minutes")
# print(d, f" {d.used_seats}/{d.seats} taken seats , time left is {d.time_left} minutes")
#
#
# print(farchis.next_available_table(7))
# farchis.get_reserved_tables
farchis.status()