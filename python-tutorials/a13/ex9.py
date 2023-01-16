start_range = int(input("Insert the start of the range: "))
end_range = int(input("Insert the end of the range: "))
for num in range(start_range, end_range+1):
    has_divisor = False
    for i in range(2, num):
        if num % i == 0:
            # num is not a prime number
            has_divisor = True
            break

    if not has_divisor:
        # num is a prime number
        print(f"{num} is prime")