# diamond shape pattern

num = int(input("Insert a number: "))

for i in range(1, num*2+1, 2):
    padding = (num*2-i) // 2 + 1
    print(" " * padding, i * "*", sep="")

for i in range(num*2+1, 0, -2):
    padding = (num*2-i) // 2 + 1
    print(" " * padding, i * "*", sep="")