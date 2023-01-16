num = int(input("Insert a number: "))

for i in range(1, num+1):
    # in each line we print i stars padded by (num - i) spaces from both sides
    padding = (num-i)
    print(" " * padding, i * "* ", sep="")