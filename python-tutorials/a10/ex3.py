nums_sum = 0
nums_count = 0
num = ''
while num != '$':
    num = input("Insert a num or $ to finish: ")
    if num.isdigit():
        num = int(num)
        nums_count += 1
        nums_sum += num
print(f"The sum is: {nums_sum}, the avg is: {nums_sum/nums_count}")