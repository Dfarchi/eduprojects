# A1
i = 1
while i <= 10:
    print(i)
    i += 1

# A2
num = int(input("Insert a number"))
count = 0
while num != 0:
    num = num // 10
    count = count + 1
print("Total digits are:", count)

# A3
num = int(input("Insert a num: "))
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)