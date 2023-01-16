# drink_type = input("Insert drink: ")  # water / beer /wine
#
#
# if drink_type == 'water':
#     print("you can drive")
# if drink_type == 'beer' or drink_type == 'wine':
#     qty = float(input("Insert qty"))
#     # continue with checks
#
#
# if drink_type == 'water':
#     print("you can drive")
# else:
#     qty = float(input("Insert qty"))
#     # continue with checks

######
# string methods
######

# operators + - <=
# built-in functions: print(), input(), round(), int()
# methods: text.upper()
import string

text = "The sun is shining and the life is beautiful!"
# print(text.upper())
# new_text = text.lower()
# print(new_text)
# print(type(new_text))
# text.split()
# ret_val = text.split(" ")
# print(ret_val)
# print(type(ret_val))
# print(ret_val[::-1])


# lists
my_list = []
my_list = ["Hello", 'World']
grades = [90, 95, 97, 85]
# print(grades[2])
various_list = ["Hello", [], True, 5.733, 78,
                ["aaa", 'bbb', [1,2,3,4]]]
# various_list[2] #bool
# various_list[3] #float
# print(various_list[-1])
# temp = various_list[-1]
# print(temp)
# temp[0] #aaa
# various_list[-1][-1][2]
# various_list[1][1]  #error
# grades[7]
# print([3, 4, 5])
# print([3, 4, 5][0]) # prints 3
# print([3, 4, 5], [0]) # prints 2 lists
# t = [3, 4, 5]
# print(t[0])

# l1 = [[2, 3, 4], [20, 30, [40]]]
# print(l1[-1][-1] > 30) # WRONG!
# print(int(l1[-1][-1]) > 30) # WRONG!
# print(l1[-1][-1][0] > 30)

# more built-in functions
# print(len(grades))
# print(len(text))
# print(text)
# print(text[3] == ' ')
# print(len(""))
# print(len([]))
# print(type(len([])))
# print(type(len))
# print(len(5))
# seats = input("Insert seats: ")
# split_seats = seats.split(" ")
# print(split_seats)
# print("split_seats[0]=", split_seats[0])
# if len(split_seats) == 2

#operator in
# grades = [90, 95, 97, 85]
# print(50 in grades)
# print(97 in grades)

# print(text)
# print("THE" in text)
# print("the" in text.lower())
#
# drink_type = input("Insert drink").lower()
# if drink_type.lower() == 'beer':

# more string methods
# print(text)
ret_val = text.find("sun")
ret_val = text.find("the")
ret_val = text.find("i")
ret_val = text.find(" ")
ret_val = text.find(" ", 10)
# look for a space starting from the word "shining"
shining_idx = text.find("shining")
ret_val = text.find(" ", shining_idx)

ret_val = text.find("blabla")
ret_val = text.index(" ")
ret_val = text.index("shining")
# ret_val = text.index("blabla")
ret_val = text.count(" ")
ret_val = "    the sun        ".strip()
ret_val = "    The Sun        ".strip().lower().index("s")
# ret_val = "    The Sun        ".strip().lower().index("s").lower() #wrong
# ret_val = text.endswith("!")

# words_list = text.split(" ")
# ret_val = "_".join(words_list)
# ret_val = "_$blabla$_".join(words_list)
# ret_val = "_".join(["aaaa", "bbbb"])
# print(words_list)

# ret_val = text.replace(" ", "_")
#
# hours = 9
# minutes = 20
# seconds = 8
# ret_val = ":".join([str(hours), str(minutes), str(seconds)])
# print(ret_val)

# list methods
# l1 = []
# g1 = int(input("insert g1 "))
# g2 = int(input("insert g2 "))
# r1 = l1.append(g1)
# print(f"new l1: {l1}")
# print(f"return value of append: {r1}")
# print(l1.append(g1))
# l1.append(g2)
# print(l1)
# new_text = text.lower()
# l1.append("gfd")
# print(l1)
# l1.append(g1)
# print(l1)
# l1.append(g2)
# print(l1)
# l1.pop(0)
# l1.remove(90)
# print(l1)
# l2 = [10, 20, 30, 50]
# print(l2)
# l2.insert(3, 40)
# print(l2)
#
# l3 = [90, 50, 67, 50]
# print(l3.count(50))
print(string.digits)
