# year = input("Your birth year: ")
# year_as_int = int(year)
#
#
#
# year = input("Your birth year: ")
# year = int(year)
#
# year = int(input("Your birth year: "))
# age = 2022 - year
# print("You are", age, "years old")

# print("You are", 2022 - int(input("Your birth year: ")), "years old")

# name = "Valeria"
# name = 'Valeria'
# s = 'She said: "My name is Valeria"'
# s = "She said:\n'My name is\t Valeria'"
# print(s, end=" blabla blabla ")
# print(name)

# my_text = "JanuaryFabruaryMarch"
#
# my_text = "January" \
#           "Fabruary" \
#           "March" \
#           "April"
#
# my_text = "January\n" \
#           "Fabruary\n" \
#           "March\n" \
#           "April"
#
# my_text = """January
# February
# MArch
# April"""
# print(my_text)

# my_text = "The sun in shining!"
#
# print(my_text[5:8])
# print(my_text[5:])
# print(my_text[:5])
# print(my_text[-1])
# print(my_text[-1:-5])
# print(my_text[-5:-1])
# # last 5 char
# print(my_text[-5:])
# print(my_text[2:10:2])
# print(my_text[10:2:-1])
# print(my_text[-1::-1])
# print(my_text[::-1])

# my_bool = True
# print("my_bool", type(my_bool))
# my_str = "True"
# print("my_bool", type(my_str))

# print("5>7?", 5>7)
#
# num = 6
# print("num==6 ?", num == 6)
#
# num = 6
# print("num != 6 ?", num != 6)
#
# num = 6
# print('6' == 6)
#
# num = 6
# print(6.0 == 6)


# print(True and True)
# # False and True
# print(True and False)
# # False and False


# print(True or True)
# False or True
# print(True or False)
# False or False

#
# drink = input('Drink: ') #beer / wine
# qty = float(input('Qty: '))
#
# can_drive = (drink == 'beer' and qty <= 0.3) or \
#             (drink == 'wine' and qty <= 0.2)
# print("Can drive:", can_drive)
#
# can_drive_after_beer = drink == 'beer' and qty <= 0.3
# can_drive_after_wine = drink == 'wine' and qty <= 0.2
# can_drive = can_drive_after_beer or can_drive_after_wine
# print("Can drive:", can_drive)


# year = int(input("Insert year: "))
# print(not(year % 4) and not(year % 100))
# print(bool("adasd"))
# is_leap_year = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

# print(bool(''))

# is_leap_year = None
# year = int(input("Insert year: "))
# is_leap_year = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

player1 = input("Player 1 turn") # scissors / paper / stone
if player1 != 'paper' and player1 != 'scissors' and player1 != 'stone':
    print("Invalid turn")
else:
    player2 = input("Player 2 turn")
    if player2 == 'paper' or player2 == 'scissors' or player2 == 'stone':
        if player1 == player2:
            print('Draw')
        else:
            if player1 == 'paper':
                if player2 == 'scissors':
                    print("Player 2 wins")
                else:
                    # player 2 is with stone for sure
                    print("Player 1 wins")