# just to save ten lines------------------------------------------------------------------------------------------------

def yes_or_no(x: str) -> str:
    while True:
        if x == 'yes':
            return 'yes'
        elif x == 'no':
            return 'no'
        else:
            x = input("has to be yes or no-").lower()
