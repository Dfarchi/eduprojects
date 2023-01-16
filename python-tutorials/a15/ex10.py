my_list = ['AAA', [4, 5, 7], "5", 5,  3.0, True, 2654, -4, 0]


for elem in my_list:
    type_name_only = str(type(elem)).replace('<class','').replace('>','').replace("'","")
    print(f"{elem} - {type_name_only}")