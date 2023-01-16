strs = ["dog","racecar","car"]

ret_val = ''
count = 0
word_short = min(strs, key=len)
for i in range(len(word_short)):
    comb = word_short[:i + 1]
    for j in strs:
        if comb == j[:i + 1]:
            count += 1
    if len(strs) == count:
        comb_l = comb
    count = 0

return comb_l

print(ret_val)