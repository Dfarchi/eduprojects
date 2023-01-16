num = int(input("Insert a number: "))

for i in range(1, num+1):
    for j in range(1, i+1):
        print(j, sep=" ", end="")
    print()