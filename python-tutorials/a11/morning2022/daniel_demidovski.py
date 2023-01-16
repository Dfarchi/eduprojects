# Time for Coffee! v2 >:D
coffee_list = [' ESPRESSO', ' DOPPIO', ' LUNGO', ' RISTRETTO', ' MACCHIATO', ' CORRETTO', ' CON PANNA', ' ROMANO',
               ' CAPPUCCINO', ' AMERICANO', ' CAFE LATTE', ' FLAT WHITE', ' MAROCCHINO', ' MOCHA', ' BICERIN', ' BREVE',
               ' RAFCOFFEE', ' MEAD RAF', ' VIENNA COFFEE', ' CHICIKATE MILK', ' LATTE MACCHIATO', ' GLACE', ' FREDDO',
               ' IRISH COFFEE', ' FRAPPE', ' CAPPUCCINO FREDDO', ' CARAMEL FRAPPE', ' ESPRESSO LACCINO']
exclude_list = []

# Function for calculating the coffee type index number
# h = hour, m = minute, indx = user/friend number
def calculate_drink(h, m, indx, *kwargs):
    if kwargs:
        opt = kwargs[0]
        return ((h + m * (indx - 1) % len(coffee_list)) + opt)
    else:
        return (h + m * (indx - 1) % len(coffee_list))

# Wrong input handling almost anything that can go wrong will go wrong but it still here
while True:
    # Get user input for the current time in 24h format
     current_time_str = input("Please insert time in 24h format (HH:MM): ").replace(":", "").strip()
     if len(current_time_str) > 4:
         print("INVALID! Please insert time in 24h format (HH:MM).")
         continue
     if not current_time_str.isdigit():
         print("INVALID! Please insert digits in 24h format with : (HH:MM).")
         continue
     else:
         hours, minutes = int(current_time_str[:2]), int(current_time_str[-2:])
         print(hours, minutes)
         if hours > 23:
            print("INVALID! Please make sure to type valid hour.")
            continue
         if minutes > 60:
            print("INVALID! Please make sure to type valid minutes.")
            continue
         else:
            break

# Wrong input handling
while True:
    # Get user input for the current people that want to drink
    friends_n = int(input("How much people drinking: ").strip())
    if friends_n <= 0:
        friends_n = int(input("INVALID! 0 People drinking? try again."))
        continue
    else:
        break

# Get user input if wanted to start from spesific type number
starting_point = int(input("If you interested in starting number for type please insert it, if not just press 0: ").strip())
# Checker
if starting_point > 0:
    starting_point = starting_point
else:
    pass

# Get user input if wanted to exclude spesific types
exclude_points = input("If you interested in excluding coffee types please insert them (1 2 3...), if not just type 0: ")
# Checker
if exclude_points != "0":
    tmp_list = exclude_points.split(" ")
    for n in tmp_list:
        exclude_list.append(int(n))
else:
    pass

# Set y as friends number
y = friends_n
# Go on all indexes
while True:
    if starting_point > 0:
        coffee_num_f_s = calculate_drink(hours, minutes, friends_n, starting_point)

        if coffee_num_f_s in exclude_list:
            coffee_num = coffee_num_w_s+1
        else:
            coffee_num = coffee_num_f_s
    else:
        coffee_num_f = calculate_drink(hours, minutes, friends_n)

        if coffee_num_f in exclude_list:
            coffee_num = coffee_num_f+1
        else:
            coffee_num = coffee_num_f
    # if still anyone didn't get calculation continue
    if friends_n > 0:
        coffee_num %= len(coffee_list)
        print(f"The {friends_n} will have #{coffee_num}{coffee_list[coffee_num - 1]}")
        friends_n -= 1
    # if friends_n == 0 break the loop
    else:
        break