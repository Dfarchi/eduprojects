from datetime import datetime


class Ravkav:

    def __init__(self, Id, name, balance):
        self.__id = Id
        self.__name = name
        self.balance = balance
        self.log = {}

    def __str__(self):
        return str(Ravkav)

    def topup(self, amn):
        self.balance += amn

    def typeride(self, km):
        ridetype = {'short': 5.5, 'med': 12, 'long': 23}
        if km < 15:
            return ['short', ridetype['short']]
        elif 15 <= km < 40:
            return ['med', ridetype['med']]
        elif 40 <= km:
            return ['long', ridetype['long']]

    def ride(self, km):
        self.balance -= self.typeride(km)[1]
        while self.balance <= 0:
            print("no credit in care plz top up, we charged you for 50 NIS")
            self.topup(50)
        if not self.log:
            self.log[datetime.date] = [self.typeride(km)]
        else:
            self.log[datetime.date].append(self.typeride(km))

    def get_rides_by_date(self, date):
        return len(self.log[date])

    def get_rides_by_type(self, date, ridetype):
        counter = 0
        for ride in self.log[date]:
            if ride[0] == ridetype:
                counter += 1
        return int(counter)


a = Ravkav('312427107', 'yuval', 10)
a.ride(15)
a.ride(17)
a.ride(10)
a.ride(50)
a.ride(5)
b = a.get_rides_by_date(datetime.date)
d = a.get_rides_by_type(datetime.date, 'med')
c = a.get_rides_by_type(datetime.date, 'short')
e = a.get_rides_by_type(datetime.date, 'long')
print(f"by date-{b}: short- {c} med-{d} long- {e} ")
print(a.balance)
a.ride(40)
print(a.balance)
