def romanToInt(s: str) -> int:
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sahac, p = 0, 0
    for letter in reversed(s):
        if romans[letter] < p:
            sahac -= romans[letter]
        else:
            sahac += romans[letter]
        p = romans[letter]
    return sahac
