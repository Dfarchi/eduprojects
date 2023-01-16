# def print_greeting():
#     print("***************")
#     print("****Hello******")
#     print("***************")
#
# # def print_greeting_name(name):
# #     print(f"Hello {name}")
#
# def print_greeting_name(name, last_name):
#     print("Before print_greeting")
#     print_greeting()
#     print(f"Hello {name} {last_name}")
#
# # print_greeting()
# print_greeting_name('Liav', 'Tausi')
# print("bye")

# detect whether this is a leap year
# year = int(input("Enter a year: "))
# if (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
#     print('not leap')
# else:
#     print('leap')


# # another task: given a month and a year, print number of days in that month
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# if month != 2:
#     if (month <= 7 and month % 2 == 1) or (month > 7 and month % 2 == 0):
#         print("31 days")
#     else:
#         print("30 days")
# else:
#     if (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
#         print("28 days")
#     else:
#         print("29 days")

#
#
# # rewriting to functions
# x = "Awesome"
#


def is_leap_year(year: int) -> bool:
    not_leap: bool = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)
    # print(f"not_leap: {not_leap}")
    return not not_leap



# year = int(input("insert a year: "))
# is_leap = is_leap_year(year)
# if is_leap:
#     print("Leap year")
# else:
#     print("Regular year")



def is_31_days_month(month):
    return month in (1, 3, 5, 7, 8, 10, 12)

print(is_31_days_month(2))


def days_in_month(month, year):
    if month != 2:
        if is_31_days_month(month):
            return 31
        else:
            return 30
        # return 31 if is_31_days_month(month) else 30
    else:
        if is_leap_year(year):
            return 29
        else:
            return 28
        # return 29 if is_leap_year(year) else 28
#
#
month = int(input("Enter month: "))
year = int(input("Enter year: "))
print(f"Days number: {days_in_month(month, year)}")
#
# print(x)
