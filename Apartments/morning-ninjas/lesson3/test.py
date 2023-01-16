n = int(input("Please insert a number: "))
stars = "*"
while len(stars) <= n:
    print(stars)
    stars = stars + "*"
stars = stars[:-1]
while len(stars)-1 != 0:
    stars = stars[:-1]
    print(stars)