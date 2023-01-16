from functools import cache, lru_cache


def name(s):
    consec = 0
    ret_val = 0
    for ind, num in enumerate(s):
        if ind == 0:
            continue
        if num != s[ind-1]:
            ret_val += consec
    return ret_val

print(name('0011001'))
cache()
lru_cache()