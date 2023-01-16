#1 - not prime
#2 = prime
#3 = prime
#4 - 4/2 = 2 - not prime
#9 - 9/3 = 3 not prime
# 15 - 15/5 = 3  15/3 = 5 not prime

# 4 -> 2, 3
# 6 ->  2, 3, 4, 5,
# 6 /2 ? -> not prime
# 5 -> 2, 3, 4
# 5 / 2? => 5 /3 ? => 5/4?

def is_prime(num: int) -> bool:
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(5))
