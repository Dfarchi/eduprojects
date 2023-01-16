def get_time_part(h_or_m, idx, split_list):
    return int(split_list[idx].replace(h_or_m, ""))

def get_minutes_delay(delay):
    split_list = delay.split(' ')

    hours = 0
    minutes = 0

    if len(split_list) == 2:
        # hours = int(split_list[0].replace("h", ""))
        # minutes = int(split_list[1].replace("m", ""))

        hours = get_time_part("h", 0, split_list)
        minutes = get_time_part("m", 1, split_list)

    elif len(split_list) == 1:
        if "m" in split_list[0]:
            # minutes = int(split_list[0].replace("m", ""))
            minutes = get_time_part("m", 0, split_list)
        elif "h" in split_list[0]:
            # hours = int(split_list[0].replace("h", ""))
            hours = get_time_part("h", 0, split_list)

    return hours * 60 + minutes

def bus_key(bus):

    # status key
    status_map = {'great': 1, 'good': 2, 'bad': 3}
    status_key = status_map[bus['status']]

    # delay key
    delay_key = 0
    for delay in bus['delays']:
        delay_key += get_minutes_delay(delay)

    # name key
    name_key = bus['name']

    return status_key, delay_key, name_key


if __name__ == '__main__':
    buses = [
        {
            "delays": ['1h 20m', '25m', '3h', '2h 1m'],
            "status": 'bad',
            "name": "Jacob",
            "route_num": 560
        },
        {
            "delays": ['20m', '5m', '3h'],
            "status": 'great',
            "name": "Moshe",
            "route_num": 769
        },
        {
            "delays": ['2h 3m'],
            "status": 'good',
            "name": "Jack",
            "route_num": 766
        },
        {
            "delays": ['6h'],
            "status": 'great',
            "name": "Mark",
            "route_num": 876
        },
        {
            "delays": ['2h 3m'],
            "status": 'good',
            "name": "Anna",
            "route_num": 456
        },
    ]
    print(list(sorted(buses, key=bus_key)))