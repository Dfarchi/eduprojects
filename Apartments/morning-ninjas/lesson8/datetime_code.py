from datetime import date, time, datetime, timedelta

today_date = date.today()
print(today_date)

now = datetime.now()
print(now)

print(now.weekday())

print(f"weekday today: {today_date.weekday()}")
in_2023 = today_date.replace(year=2023)
print(f" at 2023: {in_2023}, weekday: {in_2023.weekday()}")

# new_date = date(2022, 2, 29)

td = timedelta(days=3, hours=10)

print(now + td)

#11.11.2023 + 3 days
#11.11.2023 - 30.11.2022

dt1 = datetime(2023, month=11, day=5)
print(dt1 - now)

start_time = datetime.now().replace(minute=9)
limit = timedelta(hours=1, minutes=30)
expected_end_time = start_time + limit
time_left = expected_end_time - datetime.now()

#https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
d1 = datetime.strptime("4-Nov-2023 (14:55:00)", "%d-%b-%Y (%H:%M:%S)")
print(d1)
#November 4th, 2023, and the time is 2:55PM
print(d1.strftime("%B %Dth, %Y, and the time is %I:%M%p"))



