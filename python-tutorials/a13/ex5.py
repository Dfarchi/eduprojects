dates_num = 5
seasons = ('winter', 'summer', 'autumn', 'spring')
dates_per_season = ([], [], [], [])

for i in range(dates_num):
    date = input("Insert date: ")
    date_split = date.split(".")
    month = int(date_split[1])
    # _, m, _ = date.split(".")
    # month = int(m)
    if month in (12, 1, 2):
        dates_per_season[0].append(date)
    elif month in (3, 4, 5):
        dates_per_season[3].append(date)
    elif month in (6, 7, 8):
        dates_per_season[1].append(date)
    else:
        dates_per_season[2].append(date)

for i, season in enumerate(seasons):
    print(f"You inserted {len(dates_per_season[i])} dates in {season}:")
    for j in dates_per_season[i]:
        print(j)