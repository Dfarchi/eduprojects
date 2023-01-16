num = int(input("Insert a number: "))

for row_num in range(1, num+1):
    # in each line we print i stars
    # print(i * "*")
    for j in range(1, row_num+1):
        print("*", sep="", end="")
    print("\n", sep="", end="")

for row_num in range(num, 0, -1):
    # in each line we print i stars
    # print(i * "*")
    for j in range(row_num, 0, -1):
        print("*", sep="", end="")
    print("\n", sep="", end="")


