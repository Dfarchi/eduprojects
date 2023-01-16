list1 = []
count = 0
stop = "$"

while True:
    num = input("enter number:")
    list1.append(num)
    count += 1
    if num == stop:
        list1.remove(stop)
        break

for i in range(0, len(list1)):
    list1[i] = int(list1[i])
sm = sum(list1)

print(sm)
print(sm / count)
print(list1)