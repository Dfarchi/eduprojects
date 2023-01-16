import string


def get_indexes(letters: list):
    return list(map((' ' + string.ascii_lowercase).index, (map(str.lower, letters))))


def filter_vowels(word: str):
    li = filter(lambda letter: letter.lower() not in ('a', 'e', 'i', 'o', 'u'), 'word')
    return "".join(li)


def sort_by_ken(name_list: list):
    return sorted(name_list, key=lambda l: len(l))


def better_status(some_dict: dict):
    if some_dict['status'] == 'great':
        return 2
    elif some_dict['status'] == 'good':
        return 1
    elif some_dict['status'] == 'bad':
        return 0

# "delays": ['1h 20m', '25m', '3h', '2h 1m']
def tot_min(some_dict: dict):
    relevent = some_dict['delays']
    summ = 0
    for elem in some_dict['delays']:
        for num in elem.split(' '):
            if num.isdigit() and relevent[relevent.index(num)+1] == 'H':
                summ = num * 60
            elif num.isdigit and relevent[relevent.index(num)+1] == 'M':
                summ += num
            return summ


def sort_dict(some_list: list):
    return list(sorted(some_list, key=better_status))



if __name__ == '__main__':
    # try:
    #     print(get_indexes(['a', 'c', 'd']))
    #     # print(get_indexes([1, 'a']))
    #     print(get_indexes(['asd', 'a']))
    # except:
    #     print('not all list elements are letters')
    # print(list(filter_vowels('asdfmsawr')))
    # print(sort_by_ken(['kjb','jhvhcgk']))
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
    # print(sort_dict(buses))
    print(list(sorted(buses, key=tot_min)))
