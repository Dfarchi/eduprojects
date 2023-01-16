# Write a program that receives the length of the movie in minutes,
# and prints out the length of the movie in the following format: hh:mm.
# For example, if the input is 135, your program should print: 2h 15m

total_minutes = int(input("Insert movie length in minutes: "))
hours = total_minutes // 60
minutes = total_minutes % 60
print(f"The length of the movie is {hours}h {minutes}m")