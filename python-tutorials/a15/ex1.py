prev = 0
curr = 1
print(prev)
print(curr)
for i in range(8):
    temp = curr
    curr = prev + curr
    prev = temp
    print(curr)