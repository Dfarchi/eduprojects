import calendar
from datetime import datetime, timedelta


class DateIterator:
    def __init__(self, date: str):
        self.date = datetime.strptime(date, '%d-%m-%Y').date()
        self.month_in_date = datetime.strftime(self.date, '%d-%m-%Y').split('-')[1]
        self.year_in_date = datetime.strftime(self.date, '%d-%m-%Y').split('-')[2]
        self.max_days = calendar.monthrange(int(self.year_in_date), int(self.month_in_date))

    def __iter__(self):
        self.date = self.date
        return self

    def __next__(self):
        self.day_in_date = int(datetime.strftime(self.date, '%d-%m-%Y').split('-')[0])
        if self.day_in_date == self.max_days[1]:
            raise StopIteration
        self.date += timedelta(days=1)

        return self.date


# try:
#     for i in DateIterator('23-12-2022'):
#         print(i)
# except ValueError:
#     print('Incorrect data format, should be DD-MM-YYYY')

def date_generator(date: str):
    date = datetime.strptime(date, '%d-%m-%Y').date()

    day_in_date = int(date.day)
    month_in_date = date.month
    year_in_date = date.year

    max_days = calendar.monthrange(int(year_in_date), int(month_in_date))[1]

    for day in range(day_in_date, max_days + 1):
        yield datetime.strftime(datetime.strptime(f'{day}-{month_in_date}-{year_in_date}', '%d-%m-%Y'), '%d-%m-%Y')


z = date_generator('23-12-2022')

print(next(z))
print(next(z))


# def fib_gen(my_nums: list):
#     for num in my_nums:
#         yield b
#         my_nums.append(my_nums[-2] + my_nums[-1])
#
# my_nums = [0,1,1]
# print(next(fib_gen(my_nums)))
# print(next(fib_gen(my_nums)))