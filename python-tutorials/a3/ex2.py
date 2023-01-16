# Get 3 numbers as input and print them from the smallest to biggest
num1 = int(input("Insert num 1: "))
num2 = int(input("Insert num 2: "))
num3 = int(input("Insert num 3: "))

min_num, middle_num, max_num = None, None, None

# if num1 <= num2 and num1 <= num3:
#     min_num = num1
#     if num2 <= num3:
#         middle_num, max_num = num2, num3
#     else:
#         middle_num, max_num = num3, num2
# elif num2 <= num1 and num2 <= num3:
#     min_num = num2
#     if num1 <= num3:
#         middle_num, max_num = num1, num3
#     else:
#         middle_num, max_num = num3, num1
# else:
#     min_num = num3
#     if num1 <= num2:
#         middle_num, max_num = num1, num2
#     else:
#         middle_num, max_num = num2, num1

# print(min_num, middle_num, max_num)

# Syntactic sugar:

if num1 <= num2 and num1 <= num3:
    min_num, middle_num, max_num = (num1, num2, num3) if num2 < num3 else (num1, num3, num2)
elif num2 <= num1 and num2 <= num3:
    min_num, middle_num, max_num = (num2, num1, num3) if num1 < num3 else (num2, num3, num1)
else:
    min_num, middle_num, max_num = (num3, num1, num2) if num1 < num2 else (num3, num2, num1)

print(min_num, middle_num, max_num)