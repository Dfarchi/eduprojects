

coffee_list: list =['1# espresso','2# doppio','3# lungo','4# ristretto','5# macchiato','6# corretto','7# con panna','8# romano'
             ,'9# cappuccin','10# americano','11# cafe latte','12# flat white','13# marocchino','14# mocha','15# bicerin','16# breve',
              '17# rafcoffe','18# mead raf','19# vienna coffee','20# chocolate milk','21# latte macchiato','22# glace',
              '23# freddo','24# irish coffee','25# frappe','26# cappuccino freddo','27# caramel frappe','28# glace']
print(("""\                                                                                           
                                                  ,--.                                                      
                                ,--.   ,--. ,---. |  | ,---. ,---. ,--,--,--. ,---.                         
                                |  |.'.|  || .-. :|  || .--'| .-. ||        || .-. :                        
                                |   .'.   |\   --.|  |\ `--.' '-' '|  |  |  |\   --.                        
                                '--'   '--' `----'`--' `---' `---' `--`--`--' `----'                        
                                              ,--.                                                          
                                            ,-'  '-. ,---.  ,---.                                           
                                            '-.  .-'| .-. || .-. |                                          
                                              |  |  ' '-' '' '-' '                                          
                                              `--'   `---'  `---'                                           
                    ,--.,--.                  ,--.           ,-----.         ,---.                          
                    |  |`--' ,--,--.,--.  ,--.|  |,---.     '  .--./ ,--,--./  .-' ,---.                    
                    |  |,--.' ,-.  | \  `'  / `-'(  .-'     |  |    ' ,-.  ||  `-,| .-. :                   
                    |  ||  |\ '-'  |  \    /     .-'  `)    '  '--'\\ '-'  ||  .-'\   --.                   
                     `--'`--' `--`--'   `--'      `----'      `-----' `--`--'`--'   `----'        
 """))
manu: str = input('Would You Like to See Our Manu? ').lower().strip()
while manu not in ['yes' , 'no']:                          # Checking Users Input
    manu: str = input("\033[0;31;1m try again!: \033[0;30;0m").lower().strip()
if manu == 'yes':
    print("""\
      _                        _                                                              
     | |__   ___ _ __ ___     (_)___        ___  _   _ _ __       _ __ ___   __ _ _ __  _   _ 
     | '_ \ / _ \ '__/ _ \    | / __|      / _ \| | | | '__|     | '_ ` _ \ / _` | '_ \| | | |
     | | | |  __/ | |  __/    | \__ \     | (_) | |_| | |        | | | | | | (_| | | | | |_| |
     |_| |_|\___|_|  \___|    |_|___/      \___/ \__,_|_|        |_| |_| |_|\__,_|_| |_|\__,_|
                                                                                             """)
    print("""
     1# espresso 2# doppio 3# lungo 4# ristretto

     5# macchiato 6# corretto','7# con panna','8# romano'

     9# cappuccin 10# americano 11# cafe latte

     12# flat white 13# marocchino 14# mocha 15# bicerin'

     16# breve 17# rafcoffe 18# mead raf 19# vienna coffee

     20# chocolate milk 21# latte macchiato 22# glace

     23# freddo 24# irish coffee 25# frappe

     26# cappuccino freddo 27# caramel frappe 28# glace """)

if manu == 'no':
    quit()


remove: str = input('Would You Like to avoid any item From The list? Yes/No: ').lower().strip()              # Getting input From User
while remove not in ['yes' , 'no']:                                                                          # Checking Users Input
    remove: str = input("\033[0;31;1m try again!: \033[0;30;0m").lower().strip()
if remove == "yes":                                                                                          # user wants to remove an item
    remove_idx: str = (input('Please Insert The Number of The item? '))                                      # Getting input From User
    while (not remove_idx.isdigit()) or (int(remove_idx) > len(coffee_list)):                                                                          # Checking Users Input
        remove_idx: str = (input("\033[0;31;1m try again!: \033[0;30;0m"))
    coffee_list.pop(int(remove_idx))  # Removing the item by index
    print('\033[0;31;1m Item Has been avoided!\033[0;37;0m')
else:
    pass
time: str = (input('When Would You Like Your Coffee? ')).strip()                                             # Getting Time From User
while (len(time) != 5) or not time[3].find(':') :
    time: str = (input("\033[0;31;1m try again!: \033[0;30;0m"))
    for i in range(4):
        if i==2:
            i+=1
        if not time[i].isdigit():
            time: str = (input("\033[0;31;1m try againfu!: \033[0;30;0m"))
time_s: list = time.split(':')                                                                               # Spliting Time input By ':'
hours: int = (time_s[0])                                                                                     # Turning input To Hours int
minutes: int = (time_s[1])                                                                                   #Turning input To Minutes in
friends: str = (input('With How Many Firends? '))                                                            # Getting Amount of Friends From User cheking for *int*
while not friends.isdigit() or int(friends) < 0:                                                             # Checking Users Input
        friends: str = str(input("\033[0;31;1m try again!: \033[0;37;0m "))
time_h: int = int(hours)                                                                                     #Assigning for loop
time_m: int =int(minutes)                                                                                    #Taking user into account
special_inp: str = input('Any Special Request? Yes/No? ').lower().strip()                                    # Getting input From User
while special_inp not in ['yes' , 'no']:                                                                     # Checking Users Input
    special_inp: str = input("\033[0;31;1m try again!: \033[0;37;0m").lower().strip()                        # Getting input From User
if special_inp == "yes":
    special: int = int(input('Special Request Number? '))                                                    # Getting input From User
else:
    special = 0
pass
friends = int(friends)
friends += 1
for i in range(int(friends)):                                        #looping for amount of friends + user
 for j in range(1):                                                  #looping for amount of hours + user
  time_h+=(special)
 print('='*30)
 print(f"\t\t{coffee_list[(time_h)]}")                               #Printing the coffee based of the Hours
 print('='*30)
 time_h += time_m                                                    #Adding Hours and Minutes for friends and special number
 if time_h > 24:                                                     #reseting to 24 Hours
  time_h %= 24
