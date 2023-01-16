def romanToInt(s: str) -> int:
    mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    ret_val = 0
    s_len = len(s)
    i = 0

    while i < s_len:

        # check whether smaller roman value comes before larger
        if i+1 < s_len and mapping[s[i]] < mapping[s[i+1]]:
            ret_val += mapping[s[i+1]] - mapping[s[i]]
            i += 2
        elif i+2 < s_len and mapping[s[i]] == mapping[s[i+1]] == mapping[s[i+2]]:
            ret_val += 3 * mapping[s[i]]
            i += 3
        elif i+1 < s_len and mapping[s[i]] == mapping[s[i+1]]:
            ret_val += 2 * mapping[s[i]]
            i += 2
        else:
            ret_val += mapping[s[i]]
            i += 1

    return ret_val