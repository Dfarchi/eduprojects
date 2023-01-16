coffee_list = ["ESPRESSO", "DOPPIO", "LUNGO", "RISTRETTO",
               "MACCHIATO", "CORRETTO", "CON PANNA", "ROMANO",
               "CAPPUCCINO", "AMERICANO", "CAFE LATE", "FLAT WHITE",
               "MAROCCHINO", "MOCHA", "BICERIN", "BREVE",
               "REF COFFEE", "MEAD RAF", "VIENNA COFFEE", "CHOCOLATE MILK",
               "LATTE MACCHIATO", "GLACE", "FREDO", "IRISH COFFEE",
               "FRAPPE", "CAPUCCINO FREDO", "CARAMEL FRAPPE", "ESPRESSO LACCINO"]

coffee_time = input("Hi!, enter the time when you want to drink a coffee in 24h format: ").strip() #ex. 14:03
#validate input:
while not int(coffee_time[0:2]) < 23 or not int(coffee_time[3:5]) < 59 or not coffee_time[2] == ":":
    coffee_time = input("invalid time, please insert again: ")

number_of_friends = int(input("How many friends are coming to drink with you? "))

#BONUS2:
coffee_list_to_exclude = []
end_of_loop = False
while not end_of_loop:
    coffee_name = input("If you like, insert coffee name you want to be excluded, when finish or don't like to, insert '#': ")
    if coffee_name in coffee_list:
        coffee_list_to_exclude.append(coffee_name)
    elif coffee_name == "#":
        end_of_loop = True

for coffee_name in coffee_list_to_exclude:
    coffee_list.remove(coffee_name)
print(f"coffee drinks in the update list: {coffee_list}")

hours = int(coffee_time[0:2])
bonus1 = input("enter number for the starting coffee, if you don't like enter '0': ")
while not bonus1.isdigit():
    bonus1 = input("Try again - only digits: ")
bonus1 = int(bonus1)
user_coffee = coffee_list[(hours + bonus1)- 1] #coffee of the user
print(f"your coffee is: {user_coffee}")
minutes = int(coffee_time[3:5])
#
friends_list = [] #number of friends in a list for the for loop
n = 1
while n <= number_of_friends:
    friends_list.append(n)
    n += 1
for i, friend in enumerate(friends_list):
    if (hours + (friend * minutes)) < 29:
        friend_coffee = coffee_list[((hours + bonus1) + (friend * minutes)) - 1]
        print(f"the coffee of friend no.{i + 1} is: {friend_coffee}")
    else:
        x = ((hours + bonus1) + (friend * minutes)) % 28 #after getting the end of the coffee list, continue from beginning
        friend_coffee = coffee_list[x - 1]
        print(f"the coffee of friend no.{i + 1} is: {friend_coffee}")

#bonus2 to continue:
# - return the input if coffee name is not valid
# - count number of drink that been excluded
# - update number of drinks (28)