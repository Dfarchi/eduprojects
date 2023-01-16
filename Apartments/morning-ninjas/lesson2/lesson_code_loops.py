# # insert 3 grades and print avg
# count = 0
# grades = []
# grades_sum = 0
# while count < 3:
#     grade = int(input("Insert grade: "))
#     grades.append(grade)
#     grades_sum = grades_sum + grade
#     count = count + 1
# print(f"All the grades: {grades}")
# print(f"The avg is: {grades_sum / len(grades)}")


# drink_type = input("Insert drink: ").lower().strip()  #beer / wine
# while drink_type not in ["beer", "wine"]:
#     drink_type = input("Incorrect input. Insert drink: ").lower().strip()
# print(f"You inserted {drink_type}")


# while True:
#     drink_type = input("Insert drink: ").lower().strip()
#     if drink_type in ["beer", "wine"]:
#         break
# print(f"You inserted {drink_type}")

# incorrect_input = True
# while incorrect_input:
#     drink_type = input("Insert drink: ").lower().strip()
#     if drink_type in ["beer", "wine"]:
#         incorrect_input = False
# print(f"You inserted {drink_type}")

# while False:
#     pass

# ---------------------------------
end_of_input = False
temp_max = None
while not end_of_input:
    i = input("Insert num or $ to finish: ")
    if i == '$':
        end_of_input = True
    else:
        num = int(i)
        if temp_max is None:
            temp_max = num
        if num > temp_max:
            temp_max = num
print("MAx num", temp_max)




