# Write a code that receives a 4-digits number and prints out
# the leftmost and the rightmost digit of the number.

num = int(input("Insert a 4-digits number: "))
leftmost = num // 1000
rightmost = num % 10
print("The leftmost digit of", num, "is", leftmost)
print("The rightmost digit of", num, "is", rightmost)