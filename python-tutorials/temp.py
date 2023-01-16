coffee_list = ["Espresso", "Doppio", "Lungo", "Ristretto", "Macchiato", "Corretto", "Con Panna", "Romano", "Cappucino",
               "Americano", "Cafe Latte", "Flat White", "Marocchino", "Mocha", "Bicerin", "Breve", "Raf Coffee",
               "Mead Raf",
               "Vienna Coffe", "Chocolate Milk", "Latte Macchiato", "Glace", "Freddo", "Irish Coffee", "Frappe",
               "Cappuccino Freddo",
               "Caramel Frappe", "Espresso Laccino"]

employees_number = 'first time here!!!!'
time_to_drink = 'first time here!!!!'
starting_number = 'first time here!!!!'

excluded_coffies_indexs = []
excluded_coffies = []
employees_coffies = []

time_test1 = True
time_test2 = False
time_test3 = False
time_test4 = False
time_test5 = False
employees_test1 = True
start_number_test1 = True
excluded_test1 = False
excluded_test2 = False

print('Welcome to coffee app, this is our menu:\n')
for i, coffee in enumerate(coffee_list):
    print(f'{i} - {coffee_list[i]}', end=' | ')
print('\n')

while time_test1 or time_test2 or time_test3 or time_test4 or time_test5:

    if time_to_drink == 'first time here!!!!':
        msg = ''
    elif time_test1 or time_test3 or time_test4:
        msg = 'You entered wrong input, you need to enter the input in this pattern: (hh:mm)\n'
    elif time_test2:
        msg = 'You entered wrong input, you forget the ":" in the middle\n'
    else:
        msg = 'You entered wrong input, there are only 24 hours in day\n'

    time_to_drink = input(f'{msg}When you want to drink your coffe? (hh:mm) ')

    time_test1 = len(time_to_drink) != 5
    time_test2 = time_to_drink[2] != ':'
    time_test3 = not (time_to_drink[:1].isdigit())
    time_test4 = not (time_to_drink[3:].isdigit())
    time_test5 = True if (time_test2 or time_test3) else int(time_to_drink.split(':')[0]) > 24

while employees_test1:

    if employees_number == 'first time here!!!!':
        msg = ''
    else:
        msg = 'Your input is not a number,\n'

    employees_number = input(f'{msg}How many employees will drink the coffee? ')
    employees_test1 = not (employees_number.isdigit())

while start_number_test1:

    if starting_number == 'first time here!!!!':
        msg = ''
    else:
        msg = 'Your input is not a number,\n'

    starting_number = input(f'{msg}Enter starting number or press Enter to continue: ')
    if starting_number == '':
        starting_number = 0
        break
    start_number_test1 = not (starting_number.isdigit())

while True:

    if excluded_test1:
        msg = 'Your input is not a number,\n'
    elif excluded_test2:
        msg = f'You chose to exclued coffee number {coffee_to_excloued} but there are only {len(coffee_list)}\n'
    else:
        msg = ''

    if len(excluded_coffies_indexs) > 0:
        msg2 = 'another '
        msg3 = 'continue'
    else:
        msg2 = ''
        msg3 = 'get them all'

    coffee_to_excloued = input(f'{msg}Enter {msg2}coffee number to exclud or press Enter to {msg3}: ')
    if coffee_to_excloued == '':
        break
    excluded_test1 = not (coffee_to_excloued.isdigit())
    if not (excluded_test1):
        excluded_test2 = int(coffee_to_excloued) > (len(coffee_list))
        if excluded_test2:
            continue
        else:
            excluded_coffies_indexs.append(coffee_to_excloued)

excluded_coffies_indexs.sort()

for i, index in enumerate(excluded_coffies_indexs):
    excluded_coffies.append(coffee_list[int(index) - 1 - i])
    coffee_list.pop(int(index) - 1 - i)

time_to_list = time_to_drink.split(':')
coffee_counter = int(time_to_list[0]) + int(starting_number) - 1

if coffee_counter >= len(coffee_list):
    coffee_counter = coffee_counter % len(coffee_list)

employees_coffies.append(coffee_list[coffee_counter])

for emploee in range(int(employees_number) - 1):

    if coffee_counter + int(time_to_list[1]) >= len(coffee_list):
        coffee_counter = (coffee_counter + int(time_to_list[1])) % len(coffee_list)
    else:
        coffee_counter += int(time_to_list[1])

    employees_coffies.append(coffee_list[coffee_counter])

exclud_msg = '' if excluded_coffies_indexs == [] else f'\nYou chose to exclued the following coffies: {excluded_coffies}'

print(f'''
You order coffee to {time_to_drink} for {employees_number} of employees{exclud_msg}
You will get these coffies: {employees_coffies}''')