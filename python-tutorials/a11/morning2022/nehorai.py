#A11
coffe_type = ["#1 Espresso" , "#2 Doppio" , "#3 Lungo" , "#4 Ristretto" , "#5 Macchiato" , "#6 Corretto" ,
              "#7 Con-Panna" , "#8 Romano" , "#9 Cappuccino" , "#10 Americano" , "#11 Cafe-Latte" ,
              "#12 Flat-White" , "#13 Marocchino" , "#14 Mocha" , "#15 Bicerin" , "#16 Breve" , "#17 Raf-Coffee" ,
              "#18 Mead-Raf" , "#19 Vienna-Coffee" , "#20 Chocolate-Milk" , "#21 Latte-Macchiato" , "#22 Glace" ,
              "#23 Freddo" , "#24 Irish-Coffee" , "#25 Frappe" , "#26 Cappuccino-Freddo" , "#27 Caramel-Frappe" , "#28 Espresso-Laccino"]


#------------------CHECK TIME FUNCTION------------------------
def check_hour(u_time: str) -> str:
    while True:
        if u_time.count(":") != 1:
            u_time = input("Please add ':' between the hours and minuets: ")
        else:
            hours, minutes = u_time.split(":")
            if not hours.isdigit() or not minutes.isdigit():
                u_time = input("Please insert only numbers: ")
                continue
            else:
                if int(hours) > 24:
                    u_time = input("please insert hours in 24 hours format: ")
                    continue
                else:
                    if int(minutes) > 59:
                        u_time = input("please insert minuets in 60 minuets format: ")
                        continue
                    else:
                        return u_time
#------------------CHECK HOUR FUNCTION------------------------


#------------------EMPLOYES WITH USER CHECK FUNCTION----------
def if_number(usr_num: int) -> int:
    while not usr_num.isdigit():
        usr_num = input("Please insert only numbers: ")
    else:
        return usr_num
#------------------EMPLOYES WITH USER CHECK FUNCTION----------

#------------------REMOVE INDEX FUNCTION----------------------
def check_coffee(usr_index: int) -> int:
    while True:
        if usr_index == "$":
            return usr_index
        if not usr_index.isdigit():
            usr_index = input("Please insert only numbers: ")
            continue
        else:
            if int(usr_index) > len(coffe_type) or int(usr_index) == 0:
                usr_index = input(f"Theres only 28 coffees, please insert number between 1 - {len(coffe_type) - 1}: ")
                continue
            else:
                return usr_index

#------------------REMOVE INDEX FUNCTION----------------------


#------------------CHECKING VALID YES OR NO-------------------
def y_n_check(y_n: str) -> str:
    while True:
        y_n = y_n.lower()
        if not y_n.isalpha():
            y_n = input("Please insert only chars: ")
            continue
        if y_n == "y" or y_n == "n":
            return y_n
        else:
            y_n = input("Please insert valid answer (Y/N) only: ")
            continue
#------------------CHECKING VALID YES OR NO-------------------


#------------------CHECK USER AND EMP COFFEES-----------------
def coffee_sort_users(str_num , emp_num , user_time_insert , coffee_l):
    print(f"Main user coffee {coffee_l[int(user_time_insert[0]) - 1 + int(str_num)]}")
    for i in range(int(emp_num)):
        current_indx = (int(user_time_insert[0]) + int(str_num)) + ((i+1) * (int(user_time_insert[-1])))
        print(f"Employe {i+1} coffee is: {coffee_l[(current_indx % len(coffee_l)) - 1]}")
#------------------CHECK USER AND EMP COFFEES-----------------


user_time: str = check_hour(input("Please insert an hour: "))

employes_with_user: int = if_number(input("Please insert how many you gonna be (0) if you alone: "))

user_start_num: int = if_number(input("Please enter start number if you want (If you dont want please enter 0): "))

remove_index: str = y_n_check(input("Do you want to remove coffees? (Y/N): "))
if remove_index == "y":
    remove_index: int = check_coffee(input("Please insert the coffee number: (If you want to stop type '$'): "))
    while remove_index != "$":
        coffe_type.pop(int(remove_index) - 1)
        remove_index: int = check_coffee(input("Please insert another coffee number: (If you want to stop type '$'): "))

smt = coffee_sort_users(user_start_num , employes_with_user , user_time , coffe_type)
print('''
        THANK YOU!
Hope to see you here again!
      ''')