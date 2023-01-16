# Ask the user for a number. Print out whether the number is even or odd.

num = int(input("Insert a number: "))
# number is even if the remainder of the division by 2 equals 0
is_even = num % 2 == 0
print("The number is even:", is_even)
