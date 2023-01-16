# option 1
num = input('Insert a num: ')
print(num[::-1])

# option 2
num = int(input("Insert a num: "))
while num > 0:
    print(num % 10, end="")
    num = num // 10
