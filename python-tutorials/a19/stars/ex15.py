#     **     # 4' '*0' ' | 0' '*4' '
#    *  *    # 3' '*1' ' | 1' '*3' '
#   *    *   # 2' '*2' ' | 2' '*2' '
#  *      *  # 1' '*3' ' | 3' '*1' '
# *        * # 0' '*4' ' | 4' '*0' '


num = int(input("Insert num: "))
for i in range(num):
    if i == 0:
        print((num-1-i)*" ", "*", i*" ", i*" ", (num-1-i)*" ", sep="")
    else:
        print((num-1-i)*" ", "*", i*" ", (i-1)*" ", "*", (num-1-i-1)*" ", sep="")

for i in range(num-2, -1, -1):
    if i == 0:
        print((num-1-i)*" ", "*", i*" ", i*" ", (num-1-i)*" ", sep="")
    else:
        print((num-1-i)*" ", "*", i*" ", (i-1)*" ", "*", (num-1-i-1)*" ", sep="")