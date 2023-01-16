count = 0
even_cnt = 0
while count < 10:
    user_str = input("Insert a string: ")
    if len(user_str) % 2 == 0:
        even_cnt += 1
    count +=1
print(f"Total amount of strings with even len: {even_cnt}")