rows = int(input("Insert a number: "))

# num = 1
# for row in range(1, rows+1):
#     for col in range(1, row+1):
#         print(num, "", sep=" ", end="")
#         num += 1
#     print()

# improved version using padding
# https://www.delftstack.com/howto/python/python-pad-string-with-spaces/
num = 1
for row in range(1, rows+1):
    for col in range(1, row+1):
        print(f"{num:^5}", "", sep=" ", end="")
        num += 1
    print()