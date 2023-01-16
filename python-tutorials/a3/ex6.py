# Write a code that receives the year as input and prints whether t
# he year is a leap year or not. To be a leap year,
# the year number must be divisible by four –
# except for end-of-century years, which must be divisible by 400.
# This means that the year 2000 was a leap year, although 1900 was not.
# 2020, 2024 and 2028 are all leap years.

year = int(input("Insert year: "))
is_leap_year = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
if is_leap_year:
    print(f"Year {year} is leap year")
else:
    print(f"Year {year} is not a leap year")