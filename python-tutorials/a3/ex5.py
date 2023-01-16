# Write a code that receives 3 numbers that represent a date
# (day, month, year) and prints out the season name of the date
# (winter, summer, autumn, winter).
# In addition, print out the amount of days in the month (30, 31, or 28/29 for february).
# No need to take leap years into account

day = int(input("Insert day: "))
month = int(input("Insert month: "))
year = int(input("Insert year: "))

# calculating days in month
days_in_month = 30
if month == 2:
    days_in_month = 28
elif (1 <= month <= 7 and month % 2 == 1) or \
            (8 <= month <=12 and month % 2 == 0):
    days_in_month = 31

# calculating season
season = 'winter'
if 3 <= month <= 5:
    season = 'spring'
elif 6 <= month <= 8:
    season = 'summer'
elif 9 <= month <= 11:
    season = 'autumn'

print(f"Days in {month}: {days_in_month}, season: {season}")

