def perfect(number:int ) -> bool :
    dividers = []
    if number == 0:
        return False
    for i in range (1,number):
        if number % i == 0:
            dividers.append(i)
    if sum(dividers) == number:
        return True
    else:
        return False


def perfect2(number: int) -> bool:
    dividers_sum = 0
    if number == 0:
        return False
    for i in range(1, number):
        if number % i == 0:
            dividers_sum += i
    return dividers_sum == number


print(perfect(496))