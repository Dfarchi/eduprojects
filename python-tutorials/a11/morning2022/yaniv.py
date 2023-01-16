coffee_list = ['Espresso', 'Doppio', 'Lungo', 'Ristretto', 'Macchiato',
                'Corretto', 'Con Panina', 'Romano', 'Cappuccino', 'Americano',
                'Cafe Latte', 'Flat White', 'Marocchino', 'Mocha', 'Bicerin',
                'Breve', 'Raf Coffee', 'Mead Raf', 'Vienna Coffee', 'Chocolate Milk',
                'Latte Macchiato', 'Glace', 'Freddo', 'Irish Coffee', 'Frappe',
                'Cappuccino Freddo', 'Caramel Frappe', 'Espresso Laccino']
while True:
    coffee_time = input("Please insert coffee time in 24h format (HH:MM) ")
    if len(coffee_time) < 4:
        print("You did not write the time correctly")
        continue
    if coffee_time[2] != ':':
        print("Please try again. The way you entered the time is wrong. Use `:` to between hours and minute")
        continue
    coffee_time = coffee_time.split(":")
    hours = coffee_time[0]
    minutes = coffee_time[1]
    if len(hours) != 2:
        print("The hours are not written correctly, use the HH:MM format")
        continue
    if len(minutes) != 2:
        print("The minutes are not written correctly, use the HH:MM format")
        continue
    if not hours.isdigit() or not minutes.isdigit():
        print( "Please insert digits in 24h format with : (HH:MM).")
        continue
    hours , minutes = int(hours) , int(minutes)
    if hours > 23:
        print("Impossible time. Please choose an hour between 00 and 23")
        continue
    if minutes > 59:
        print("Impossible time. Please choose an minutes between 00 and 59")
        continue
    else:
        break


while True:
    friends = input('How many friends would you like to have the coffee with?' )
    if not friends.isdigit():
        print("Please enter a whole number only")
        continue
    else:
        break
friends = int(friends)

index_list = (input("If there are types of coffee that you want to remove"
                    " from the list, enter the numbers. If not press 0 "))

string_num = input('Please enter the starting number. if you do not want to choose a number enter 0 ')
while not string_num.isdigit():
    string_num = input("Please enter a whole number only")
string_num = int(string_num)

if index_list != "0":
    index_list = index_list.split(" ")
    index_list.sort(reverse=True)
    for c in index_list:
             coffee_list.pop(int(c)-1)
    coffee_list = coffee_list
    user_ = ((string_num + hours) - 1)
    print(f"the user will receive: {coffee_list[user_]} ")
    if friends > 0:
        for d in range(1, friends+1):
            friends_order = (user_ + (minutes * d)) % 28
            print(f"for friend {d} will receive: {coffee_list[friends_order]} ")
else:
    user_ = (string_num + hours - 1)
    print(f"the user will receive: {coffee_list[user_]} ")
    if friends > 0:
        for d in range(1, friends+1):
            friends_order = (user_ + (minutes * d)) % 28
            print(f"for friend {d} will receive: {coffee_list[friends_order]} ")
