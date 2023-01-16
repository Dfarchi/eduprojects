def taz_generator():
    import random
    taz = [random.randint(0,9) for i in range(0,8)]
    taz.append(taz_check(taz))
    return ''.join(map(str, taz))


def card_generator():
    import random
    taz = [random.randint(0,9) for i in range(0,15)]
    taz.append(taz_check(taz))
    return ''.join(map(str, taz))


def taz_check(taz:list)-> int:
    sum_l=[]
    for i in range(len(taz)):
        i = int(i)
        if i%2 != 0:
            y = 2*int(taz[i])
            if y > 9:
                y = y % 10 + ((y - (y % 10))//10)
                sum_l.append(y)
            else:
                sum_l.append(y)
        else:
            y = int(taz[i])
            sum_l.append(y)
    sifrat_bikoret = 10 - sum(sum_l) % 10
    if sifrat_bikoret % 10 == 0:
        sifrat_bikoret = sifrat_bikoret//10
        return sifrat_bikoret
    else:
        return sifrat_bikoret

# print("if you want to check if an Id is real type 'check' ")
# print("if you need a new one (no questions asked) type 'new'" )
# user_input = input("well? -")
#
# while True:
#     if user_input.lower() == "check":
#         taz = [i for i in input("please fill the first 8 digits of your id here:")]
#         print("this is the taz: ")
#         print(taz)
#         taz.append(taz_check(taz))
#         print(taz)
#         break
#
#     elif user_input.lower() == "new":
#         print("your new ID is-", taz_generator())
#         break
#     else:
#         user_input = input("again")


