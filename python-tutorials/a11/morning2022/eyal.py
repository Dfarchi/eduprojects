coffee_list = ['espresso', 'doppio', 'lungo', 'ristretto', 'macchiato', 'corretto', 'con panna',
               'romano', 'cappuccino', 'americano', 'cafe latte', 'flat white', 'marocchino', 'mocha',
               'bicerin', 'breve', 'raf coffe', 'mead raf', 'vienna coffee',
               'chocolate milk', 'latte macchiato', 'glace', 'freddo',
               'irish coffee', 'frappe', 'cappuccino freddo',
               'caramel frappe', 'espresso laccino']
while True:
    time = input('welcome to our coffee place, When Would You Like drink Your Coffee? ')  # taking input from the user
    friends = int(input('how many co-workers will be joining you? '))  # taking the amout of people with the user
    time_s = time.split(
        ':')  # making list with 2 indexes the first will be the hours and the second minutes splitting by ":"
    hours = time_s[0]  # hours = index[0]
    minutes = time_s[1]  # minutes = index[1]
    if hours.isdigit() and minutes.isdigit():  # checking if the input is valid, if yes breaking the loop
        break
    else:  # if the input not correcr ill guide the user to insert the correct way
        print("please enter time with digits in the showing format: (xx:yy")
        continue  # it will repeat itself until the user inserted the correct way
hours = int(time_s[0])  # now i can asure the input is int
minutes = int(time_s[1])
time_sum = hours + minutes  # calculating the sum of hours and minutes in order to take the users guests coffee index
coffee_out = []  # making new list where ill put the names of the user + friends coffee
new_minutes = time_sum % 28
if friends == 0:  # if hes without any  friends i want to stop the program here and print his coffee
    coffee_out.append(coffee_list[hours-1])
    print(f"your coffee is: {coffee_out[0]}")
else:
    for i in range(friends+1):# for  every friend i need to calculate the coffee
        if time_sum > 28:# if the sum is bigger than  the list  i want to find the drink  if i woukldstill counting from the begining
            new_minutes += time_sum % 28
            if new_minutes > 28:
                new_minutes = new_minutes % 28
                coffee_out.append(coffee_list[new_minutes - 1])
            else:
                coffee_out.append(coffee_list[new_minutes - 1])
        else:
            coffee_out.append(coffee_list[(hours + (minutes * i)-1)])# if the sum less than the list i calculate by the friends number
            # and mutiply the minutes by the order toget all  the others coffee
            i += 1

    print(f"your coffee is {coffee_out[0]}") #(printing the users coffee
    print((f"your friends coffees are :{coffee_out[1:]}")) # printing all the friends coffeess
print("have a nice and productive day !")
