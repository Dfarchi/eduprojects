# find a bug exercise

# while loops - iterating over list
# grades = [98, 100, 97, 96, 87]
# i = 0
# while i < len(grades):
#     print(grades[i])
#     i = i + 1

# continue
# example: print all the numbers from 1 up to n,
# skipping those which digits sum is even
# num = int(input("Insert a num: "))
# i = 0
# numbers_sum = 0
# while i < num:
#     i = i + 1
#
#     digits_sum = 0
#     temp = i
#     while temp > 0:
#         digits_sum = digits_sum + temp % 10
#         temp = temp // 10
#
#     if digits_sum % 2 == 0:
#         continue
#
#     print(i)
#     numbers_sum += i


# for loops
# iterating lists, strings
# range
grades = [95, 98, 97, 100, 95]
# for grade in grades:
#     print(f"The grade is: {grade}")
# for i, grade in enumerate(grades):
#     print(f"The grade number {i+1} is: {grade}")
text = "Hello World"
# for char in text:
#     print(char)
# for word in text.split(" "):
#     print(word)

# The best options
# words_list = text.split(" ")
# print(len(words_list))
# for word in words_list:
#     print(word)

# Bad option - code duplication + less efficient,
# performs the same action twice
# words_list = text.split(" ")
# print(len(text.split(" ")))
# for word in text.split(" "):
#     print(word)

# for i, word in enumerate(text.split(" ")):
#     print(word)
#
# print(i+1)

# my_range = range(10)
# print(type(my_range))
# print(my_range)
# print(0 in my_range)
# print(10 in my_range)
# for i in range(10):
#     print(i)


# my_range = range(-10, 1, 2)
# print(0 in my_range)
# print(-9 in my_range)
# for i in my_range:
#     print(i, end=" ")

# grades = [95, 98, 97, 100, 95]
# for i in range(len(grades)-1, -1, -1):
#     print(grades[i], end=" ")

# for j, i in enumerate(range(10, -1, -1)):
#     print(f"{j+1} - {i}")

# print(sorted(grades, reverse=True))
# grades[::-1]


# nested loops
# print multiplication table (square)
# input validation - get student names and grades including validation
# 1 * 1
# 1 * 2
# 1* 3
#...
# 2 *1
#2 * 2
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i}*{j} = {i*j}")


# for i in range(1, 4):
#     num = input("Insert a number: ")
#     while not num.isdigit():
#         num = input("Try again: ")
#     print(f"Number {i} is {int(num)}")

# for i in range(1, 4):
#     num = input("Insert a number: ")
#     while not num.isdigit():
#         num = input("Try again: ")
#     num = int(num)
#     while num < 1 or num >31:
#         num = input("Insert number in range of 1 .. 31")
#         num = int(num)

    # while not num.isdigit() and (int(num) < 1 or int(num) >31):
    #     num = input("Try again: ")




    # print(f"Number {i} is {int(num)}")


# lists - assignment
# grades = [95, 90, 100]
# grades[1] = 87
# errors
# print(grades)
# grades[3] = 80
# grades.insert(3, 80)
# grades[5] = 90
# grades2 = [89, 90, 91]
# for g in grades2:
#     grades.append(g)
# grades.extend(grades2)
# grades.extend("sdfsdf")
# print(grades)


# mutability
# num1 = 35
# num2 = 45
# print(id(num1), id(num2))
# my_list = [num1, num2]
# print("my_list[0]", id(my_list[0]))
# print(id(my_list))
# print(my_list)
# num1 = 50
# print(id(my_list))
# print(my_list)
# print("my_list[0]", id(my_list[0]))
# my_list[0] = 800
# print("after my_list[0] = 800")
# print("my_list[0]", id(my_list[0]))
# l1 = [35]
# l2 = [45]
# my_list = [l1, l2]
# print(my_list)
# l1[0] = 50
# print(my_list)

# my_list = [1, 2]
# print("id(my_list[0])", id(my_list[0]))
# print("id(my_list[1])", id(my_list[1]))
# my_list.insert(1, 3)
# print("id(my_list[0])", id(my_list[0]))
# print("id(my_list[1])", id(my_list[1]))
# print("id(my_list[2])", id(my_list[2]))
# print(my_list[0] is my_list[1])
# print(id(my_list[0]) == id(my_list[1]))

# name1 = input("insert name1: ")
# name2 = input("insert name2: ")
# print("name1 == name2", name1 == name2)
# print("name1 is name2", name1 is name2)

# name1 = "aaa"
# name2 = "aaa"
# print("name1 == name2", name1 == name2)
# print("name1 is name2", name1 is name2)

# name1 = 111
# name2 = 111
# print("name1 == name2", name1 == name2)
# print("name1 is name2", name1 is name2)

# name1 = int(input("insert num"))
# name2 = int(input("insert num"))
# print("name1 == name2", name1 == name2)
# print("name1 is name2", name1 is name2)


# num1 = 50
# print(id(num1))
# num1 = 55
# print(id(num1))

# vs
# l1 = []
# print(id(l1))
# l1.append(5)
# print(id(l1))
# # vs
# l1 = [5]
# print(id(l1))


# num2 = 60
# print(id(num2))
# num2 = num1
# print(id(num2))
# x = input("text:  ")
# y = input("text:  ")
# x = "apple"
# y = "apple"
# x = []
# y = []
# print(x == y)
# print(x is y)
# print(id(x), id(y))

# l = [['Paris', 'London', 'New York'],
#      [45, True, 5.5, 'hello'], -3,
#      [5, ['#', '$', '%', '^', [10, 20, 30, 40]]],
#      [['a'], ['b'], 'c', [['d']]]]
# cities = l[0]
# numbers = l[3][1][4]
# numbers = l[3][1][4] = "www"
# l[3][1][4] = "www"
# cities = "World"
# cities[0] = "Tel Aviv"
# print(l)
# print(numbers)

# s = "Paris"
# s_lower = s.lower()
# print(s is s_lower)

# names = []
# grades = []
# for name_idx in range(3):
#     grades.append([])
#     names.append(input("Insert a name"))
#     for grade_idx in range(2):
#         grades[name_idx].append(int(input("insert grade: ")))
# print(names, grades)

# names = ['VAleria', 'Shay', 'Ziv']
# names1 = names.copy()
# names2 = names
# print(names is names2)
# print(names is names1)

# names = [["Shay", "Ziv"],
#          ["Nehorai"],
#          ["Noa", "Tamar"]]
# names1 = names.copy()
# names[0][0] = "Valeria"
# names1[0][0] = "VVVVVV"
# print(names1)
# print(names)
# print(names is names1)

# import copy
# copy.deepcopy(names)


# functions
# no params, no return values
# params
# return values
# insert a month, insert a year
# while True:
#     year = input("insert a year: ")
#     if year.isdigit():
#         year = int(year)
#         break
# while True:
#     month = input("insert a month: ")
#     if month.isdigit():
#         month = int(month)
#         break


def get_num_from_user(message):
    while True:
        num = input(message)
        if num.isdigit():
            num = int(num)
            return num
# print(get_year)
# get_year

my_year = get_num_from_user("insert a year")
my_month = get_num_from_user("insert a month")
print(my_year, my_month)
# print(year)
# month = get_month()
# print(f"{year} - {month}")


cities = ['New York', 'Kyiv', 'Paris', 'London', 'Tel Aviv']
countries = ['USA', 'Ukraine', 'France', 'UK', 'Israel']
names = ['Moshe', 'Orly', 'David', 'Jack', 'Ofer', 'James']
various = ['AAA', [4, 5, 7], "5", 5,  3.0, True, 2654, -4, 0]