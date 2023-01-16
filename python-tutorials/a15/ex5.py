n = 5
# first number of sequence
start = 2
sum_seq = 0
end_char = "+"

# run loop n times
for i in range(0, n):
    if i == n-1:
        end_char = "="
    print(start, end=end_char)
    sum_seq += start
    # calculate the next term
    start = start * 10 + 2
print(sum_seq)