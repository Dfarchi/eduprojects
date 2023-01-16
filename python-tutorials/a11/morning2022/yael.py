import random
import sys, time, os


#  -------------  function  --------------------------------------------------------------------------------------------

# this function receive from the user an hour in the requested format, checks if the format is correct
# and returns the hour value and the minute value
def time_check():
    while True:
        time = input("\nEnter the time of the day in format HH:MM : ").strip()
        n = 0

        # check if the user enter just string and ask him to insert a new input
        if time.isalpha():
            print("\n\033[4;1;31m INVALID INPUT! \n please insert numbers and not string in format HH:MM \033[1;0m")
        # the else check if we have in the input one ':'
        else:
            for i in time:
                if i == ":":
                    n += 1

            if n == 1:
                time_l = time.split(":")
            else:
                print("\n\033[4;1;31m WRONG FORMAT! please insert in format HH:MM \033[1;0m")
                continue

            if len(time_l) == 2:
                if time_l[0].isdigit():
                    if 0 <= int(time_l[0]) <= 24:
                        hh = int(time_l[0])
                        if time_l[1].isdigit():
                            if 0 <= int(time_l[1]) <= 60:
                                mm = int(time_l[1])
                                return hh, mm
                            else:
                                print("\n\033[4;1;31m The minutes is out of range, please try again \033[1;0m")
                        else:
                            print("\n\033[4;1;31m The minutes should be a number. please try again \033[1;0m")
                    else:
                        print("\n\033[4;1;31m The hour is out of range, please try again \033[1;0m")
                else:
                    print("\n\033[4;1;31m The hour should be a number. please try again \033[1;0m")


# this function get from the program text and bool. The function checks if the value is a number.
# the bool variable get true if the number can be zero otherwise the variable get false.
# the function returns the number it received from the user after checking
def num_check(message, can_zero):
    while True:
        num = input(f"\n{message}")
        if can_zero :
            if num.isdigit() and int(num) >= 0:
                num = int(num)
                return num
            print("\033[4;1;31m Invalid input! please enter a number\033[1;0m")
        else:
            if num.isdigit() and int(num) > 0:
                num = int(num)
                return num
            print("\033[4;1;31m Invalid input! please enter a number\033[1;0m")


# the function checks the variable that the user entered if it's a number
def num_coffee_check(num_co):
    if num_co.isdigit() and int(num_co) >= 0:
        num = int(num_co)
        return num
    print("\n\033[4;1;31m Invalid input! please enter a number\033[1;0m")


# The function inserts into a list the numbers of the coffee that the user wants to remove from the original list
def coffee_out_() ->list:
    l_coffee_out_of = []
    while True:
        num_coffee_out = input("Enter the numbers of coffee you want to get out from the list.\n "
                               "enter a '$' in the end ")
        if num_coffee_out != "$" and num_coffee_check(num_coffee_out):
            l_coffee_out_of.append(int(num_coffee_out)-1)
        else:
            break
    return l_coffee_out_of


def coffee_out_list(cof_l) -> list:
    y_n = yes_or_no("Do you want to get out a coffee from the list?")
    if y_n == 1:
        lis_coffee_out: list = coffee_out_()

        lis_coffee_out.sort(reverse=True)
        for coffee_out in lis_coffee_out:
            cof_l.pop(coffee_out)
    return cof_l


# The function accepts a string and prints it character by character
def typrun(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != "\n":
            time.sleep(0.02)
        else:
            time.sleep(0.5)


def yes_or_no(mess):
    while True:
        roll_y_n = input(f"{mess}\n"
                         f"\033[4;1;36m 1 - for 'yes' , number 2 - for 'no': \033[1;0m").strip()
        if roll_y_n.isdigit() and int(roll_y_n) == 1:
            return 1
        elif roll_y_n.isdigit() and int(roll_y_n) == 2:
            return 2
        else:
            print("\n\033[4;1;31m Invalid input! please enter 1 or 2\033[1;0m")


def roll_a_coffee(rangend) -> int:
    return random.randrange(0, rangend)


# def roll_a_time_minutes() -> int:
#     return random.randrange(0, 60)

def milk_pik(milks_options, friend_num) -> list:
    milk_opt = []
    x = friend_num
    print("\nThese are milk options, please choose one for a person:")
    for j, i in enumerate(milks_options):
        print(j+1, i)

    person = 1
    while x > 0:
        mil = input(f"person {person}: ")
        if mil.isdigit() and 0 < int(mil) <= len(milks_options):
            milk_opt.append(int(mil)-1)
            x -= 1
            person += 1
        else:
            print("\n\033[4;1;31m Invalid input! please enter the numbers in the range\033[1;0m")
    return milk_opt


#  -------------  function  --------------------------------------------------------------------------------------------


os.system("cls")  # = clear

coffee_l = ["ESPRESSO", "DOPPIO", "LUNGO", "RISTRETTO", "MACCHIATO", "CORRETTO", "CON PANNA", "ROMANO", "CAPPUCCINO",
            "AMERICANO", "CAFELATTE", "FLAT WHITE", "MAROCCHINO", "MOCHA", "BICERIN", "BREVE", "RAF COFFEE",
            "MEAD RAF", "VIENA COFFEE", "CHOCOLATE MILK", "LATTE MACCHIATO", "GLACE", "FREDDO", "IRISH COFFEE",
            "FRAPPE", "CAPPUCCINO FREDDO", "CARAMEL FRAPPE", "ESPRESSO LACCINI"]
milk: list = ["cow's milk", "soy", "almonds", "oats"]

a="                 _  _  \n"
b="                 | || | \n"
c="  __      __ ___ | || |  ___  ___   _ __ ___    ___ \n"
d="  \ \ /\ / // _ \| || | / __|/ _ \ | '_ ` _ \  / _ \ \n"
e="   \ V  V /|  __/| || || (__| (_) || | | | | ||  __/\n"
f="    \_/\_/  \___||_||_| \___|\___/ |_| |_| |_| \___|\n"

typrun(a)
typrun(b)
typrun(c)
typrun(d)
typrun(e)
typrun(f)
print("\n \n")

user_name = input("Enter your name: ")
company_name = input("Enter your company: ")
greeting = f"\nWelcome {user_name}.\nYou have arrived at the coffee application of the company {company_name}\n" \
           f"you have the option to roast your coffee and that of your friends " \
           f"\nand you have the option to choose which coffee you want.\n\n"
typrun(greeting)

roll = yes_or_no("Do you want to roast your coffee?")
if roll == 1:
    num_friends = num_check("Enter a number of friends including you: ", False)
    choice_of_milk: list = milk_pik(milk, num_friends)
    start_num = num_check("Enter the number you want to start: ", True)

    l_without_coffee_pic = coffee_out_list(coffee_l)

    print("\nYour order is:\n")

    for i in range(num_friends):
        coffee_roll = roll_a_coffee(len(l_without_coffee_pic))
        print(f"coffee #{coffee_roll}: {l_without_coffee_pic[coffee_roll-1]}, {milk[choice_of_milk[i]]} base\n")

else:

    time_hours, time_minutes = time_check()
    # time_check return the time that the user enter after a check.
    # return hours alone and minutes alone.

    num_friends = num_check("Enter a number of friends including you: ", False)
    # function that receive a message and a bool: true - if the number can be 0, false - if the number can not be 0.
    # tha number have to be positive. return a number

    choice_of_milk: list = milk_pik(milk, num_friends)

    start_num = num_check("Enter the number you want to start: ", True)

    l_without_coffee_pic = coffee_out_list(coffee_l)

    print("\nYour order is:\n")

    # print the coffee the user has selected
    typrun(f"Coffee #{time_hours + start_num}: {l_without_coffee_pic[time_hours + start_num - 1]}, {milk[choice_of_milk[0]]} base")
    # print(f"Coffee #{time_hours + start_num} ({coffee_l[time_hours + start_num - 1]})")

    # print the friends' coffee if there are friends.
    num_friends -= 1
    if num_friends > 0:

        for friend in range(1, (num_friends+1)):
            coffee_num = time_hours + start_num + (time_minutes * friend)

            if coffee_num > len(l_without_coffee_pic):
                coffee_num = coffee_num % len(l_without_coffee_pic)
                # print(f"Coffee #{coffee_num} ({coffee_l[coffee_num-1]})")
                typrun(f"\nCoffee #{coffee_num}: {l_without_coffee_pic[coffee_num-1]}, {milk[choice_of_milk[friend-1]]} base")

            else:
                # print(f"Coffee #{coffee_num} ({coffee_l[coffee_num - 1]})")
                typrun(f"\nCoffee #{coffee_num}: {l_without_coffee_pic[coffee_num - 1]}, {milk[choice_of_milk[friend-1]]} base")










 # if len(time_l) == 2:
            #     if time_l[0].isdigit() and time_l[1].isdigit() and (1 <= int(time_l[0]) <= 24) and (
            #             1 <= int(time_l[1]) <= 60):
            #         hh = int(time_l[0])
            #         mm = int(time_l[1])
            #         return hh, mm
            #     else:
            #         print("Invalid input!")
            #         continue
            # else:
            #     print("Invalid input!")
            #     continue

    # # the list of the coffee the user want to delete from the list
    # y_n = int(input("\nDo you want to get out a coffee from the list?\n"
    #                 "\033[4;1;36m 1 - for 'yes' , number 2 - for 'no':\033[1;0m "))
    # if y_n == 1:
    #     lis_coffee_out = coffee_out()
    #
    #     lis_coffee_out.sort(reverse=True)
    #     for coffee_out in lis_coffee_out:
    #         coffee_l.pop(coffee_out)
