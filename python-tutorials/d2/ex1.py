import datetime

class DateIterator:
    def __init__(self, init_date=datetime.datetime.now()):
        self.init_date = init_date

    def __iter__(self):
        self.curr = self.init_date
        return self

    def __next__(self):
        next_day = self.curr + datetime.timedelta(days=1)
        if (next_day).month != self.curr.month:
            raise StopIteration

        self.curr = next_day
        return next_day


if __name__ == '__main__':
    my_date = DateIterator()
    for d in my_date:
        print(d)