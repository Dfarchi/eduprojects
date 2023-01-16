seat = input("Insert seat number (for example, 13B): ")
structure = input("Insert aircraft structure (for example: ABC DEFG HIJ): ")

# check whether row number is a single digit
# OPTION I
if seat[1].isdigit():
    row = seat[0:2]
else:
    row = seat[0]
# OPTION II
# if len(seat) == 2:
#     row = seat[0]
# else:
#     row = seat[:2]

# store row and seat in separate variables
row = int(row)
seat_char = seat[-1]
print(f"Row: {row} | Seat char: {seat_char}")

# get the index of the char in the structure
seat_char_idx = structure.index(seat_char)

#5B
#ABC DEF (1)

# the leftmost and the rightmost are windows
if seat_char_idx == 0 or seat_char_idx == len(structure)-1:
    print("window")

# if the char from the left of the char from the right is not space - we are in the middle
elif structure[seat_char_idx-1] != " " and structure[seat_char_idx+1] != " ":
    print("middle")

# otherwise we are for sure in the aisle
else:
    print("aisle")
