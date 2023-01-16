str_count = 0
total_chars = 0
total_digits = 0
while True:
    user_str = input("Insert a string: ")
    if user_str == '$':
        break
    else:
        str_count += 1
        total_chars += len(user_str)
        if user_str.isdigit():
            total_digits += len(user_str)

print(f"Total strings received: {str_count}")
print(f"Total chars received: {total_chars}")
print(f"Total digits received: {total_digits}")

