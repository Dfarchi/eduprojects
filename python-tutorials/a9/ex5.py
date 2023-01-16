seats = input("Enter the letters of the seats in the plane:")
count = seats.count(" ")
seats = seats.split(" ")
if count == 2:
    print(len(seats[0]), len(seats[1]), len(seats[2]))
elif count == 1:
    print(len(seats[0]), len(seats[1]))
else:
    print(len(seats[0]))