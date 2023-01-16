COMMANDS = ('signup', 'add', 'display', 'quit')


def get_command() -> str:
    while True:
        command = input("Insert command (signup, add, display, quit): ")
        if command not in COMMANDS:
            print("Invalid command, try again")
        else:
            return command


def signup(water_dict):
    username = input("Insert username: ")
    if username not in water_dict:
        water_dict[username] = {}
    else:
        print("Username already exists")


def add_water(water_dict):
    username = input("Insert username: ")
    if username not in water_dict:
        print("User does not exist")
        return

    date = input("insert date: ")
    if date not in water_dict:
        water_dict[date] = 0

    amnt = int(input("Insert amnt of glasses: "))
    water_dict[date] += amnt


def display_water(water_dict):
    username = input("Insert username: ")
    if username not in water_dict:
        print("User does not exist")
        return

    date = input("insert date: ")
    if date not in water_dict:
        print(f"0 glasses on {date}")
    else:
        print(f"{water_dict[date]} glasses on {date}")


water_dict = {}
while True:
    cmd = get_command()
    match cmd:
        case 'signup':
            signup(water_dict)
        case 'add_water':
            add_water(water_dict)
        case 'display_water':
            display_water(water_dict)
        case _:
            print("Bye")
            exit(0)

# {
#     'valeria': {
#         'dates_data':
#             {
#                 '1-1-2023': 3,
#                 '2-1-2023': 6
#             },
#         'total': 9
#     },
#     'barel': {
#         'dates_data': {
#             '2-1-2023': 10
#         },
#         'total': 10
#     }
# }