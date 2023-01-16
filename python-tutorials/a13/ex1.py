# Write a program that receives a number from a user and
# calculates the sum of all numbers from 1 to a given number

n = int(input("Enter a number: "))
s = 0
for i in range(1, n + 1, 1):
    s += i
print("\n")
print("The sum is: ", s)
