# B1
n = int(input("Enter a number: "))
s = 0
for i in range(1, n + 1, 1):
    s += i
print("\n")
print("The sum is: ", s)

# B2
n = int(input("Insert a number: "))
for i in range(1, 11):
    product = n * i
    # print(f"{i}*{n} = {product}")
    print(f"{i:5d}*{n} = {product}")

# B5
dates = []

# loop to get 10 dates as input
for i in range(4):
    dates.append(input(f"Enter date {i}: "))

winter = []
autumn = []
spring = []
summer = []


# loop to update lists
for date in dates:

    # get month from date
    month = int(date.split(".")[1])

    if month in [12, 1, 2]:
        winter.append(date)
    elif month in [3, 4, 5]:
        spring.append(date)
    elif month in [6, 7, 8]:
        summer.append(date)
    else:
        autumn.append(date)

# print results
if len(winter) > 0:
    print(f"You entered {len(winter)} winter dates: {winter}")

if len(autumn) > 0:
    print(f"You entered {len(autumn)} autumn dates: {autumn}")

if len(spring) > 0:
    print(f"You entered {len(spring)} spring dates: {spring}")

if len(summer) > 0:
    print(f"You entered {len(summer)} summer dates: {summer}")


# B5 - improved
dates = []

# loop to get 10 dates as input
for i in range(5):
    dates.append(input(f"Enter date {i}: "))

winter = []
autumn = []
spring = []
summer = []

winter_months = (12, 1, 2)


# loop to update lists
for date in dates:

    # get month from date
    month = int(date.split(".")[1])

    if month in winter_months:
        winter.append(date)
    elif month in (3, 4, 5):
        spring.append(date)
    elif month in [6, 7, 8]:
        summer.append(date)
    else:
        autumn.append(date)

# print results
season_names = ('winter', 'autumn', 'spring', 'summer')
for i, season_dates in enumerate([winter, autumn, spring, summer]):
    print(f"season_dates values: {season_dates}")
    if len(season_dates) > 0:
        print(f"You entered {len(season_dates)} {season_names[i]} dates: {season_dates}")

# B6
num = int(input('Insert a num: '))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # run loop 5 times
    for i in range(1, num + 1):
        # multiply factorial by current number
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)