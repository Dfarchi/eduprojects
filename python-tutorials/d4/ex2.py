from datetime import datetime
def map_to_date(date_as_str):
    return datetime.strptime(date_as_str, "%d-%m-%Y")

def filter_days(date_obj):
    return date_obj.weekday() not in (4, 5)

print(list(filter(filter_days, map(map_to_date, ['12-12-2021', '18-12-2021', '19-12-2021']))))