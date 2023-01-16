coffee_menu = ["Espresso", "Doppio", "Lungo", "Ristretto", "Macchiato", "Correto", "Con Panna", "Romano", "Cappuccino", "Americano", "Cafe Latte", "Flat White", "Marocchino", "Mocha", "Bicerin", "Breve", "Raf Coffee", "Mead Raf", "Vienna Coffee", "Chocolate Milk", "Latte Macchhiato", "Glace", "Freddo", "Irish Coffee", "Frappe", "Cappucino Freddo", "Caramel Frappe", "Espresso Laccino"]
drink_time = input('What time would you like to drink coffee? Please type hh:mm').split(":")
colleagues = int(input('How many colleagues will be drinking, including yourself?'))
bonus_1 = int(input('Would you like to bump the coffee list forward? If so, please enter the starting number. If not, enter 0'))

user_coffee_num = int(drink_time[0])-1+bonus_1
user_coffee = coffee_menu[user_coffee_num]
print ("You will drink", user_coffee)

if colleagues>1 :
    for colleague in range(1,colleagues) :
        colleague_coffee_num = int((user_coffee_num + (int(drink_time[1]))*colleague))
        if colleague_coffee_num <= 28 :
            colleague_coffee = coffee_menu[colleague_coffee_num]
        elif colleague_coffee_num > 28 :
            colleague_coffee = coffee_menu[colleague_coffee_num % 28]
    print ("Your colleague will have", colleague_coffee)



