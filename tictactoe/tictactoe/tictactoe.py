print('🐈🐕')
def board_updated(size: int, turn: list) -> list:
    board_lst = []
    counter = 1
    for slot in range(0, size * size):
        if counter <= 9:
            board_lst.append('|_ ' + str(counter) + '_|')
        else:

            board_lst.append('|_' + str(counter) + '_|')
        counter += 1
    board_lst[turn[0]] = ('|_' + turn[1] + '_|')
    return board_lst


def board_printer(size: int, board: list):
    ind = 0
    for col in range(0, size):
        for row in range(0, size):
            print(board[ind], end='')
            ind += 1
        print()


def row_win(size: int, turn: list, board:list) -> int():
    row_index = 0
    for line in range(0, size):
        row_counter = 1
        for row in range(0, size-1):
            if board[row_index] != ('|_ ' + turn[1] + '_|') and board[row_index] == board[row_index + 1]:
                row_counter += 1
            row_index += 1
        # row_index += 1
        if row_counter == size:
            win = 1
            print("YOU WIN ROW")
            return win


def col_win(size: int, turn: list, board: list,) -> int():
    col_count = 0
    for col_index in range(0, len(board) - size):
        if board[col_index] != ('|_ ' + turn[1] + '_|') and board[col_index] == board[col_index + size]:
            col_count += 1
            if col_count == size:
                print("YOU WIN COL")
                win = 1
                return win


# noinspection SpellCheckingInspection
def diag_win(size: int, board: list, turn:str) -> int():
    n1_count = 0
    n2_count = 0
    # left = []
    # right = []
    # [left.append(diag_index) for diag_index in range(0, len(board) - (size + 1))]
    for diag_index in [board[size+z] for z in range(0, size)]:
        if board[diag_index] != turn and board[diag_index] == board[diag_index + size +1]:
            n1_count += 1
            if n1_count == size:
                print("YOU WIN left")
                win = 1
                return win
    # [right.append(diag_index) for diag_index in range(0, len(board) - (size - 1))]
    for diag_index in [board[(size+2*z)-1] for z in range(0, size)]:
        if board[size - 1] != turn and board[size - 1] == board[diag_index + size]:
            n2_count += 1
            if n2_count == size:
                print("YOU WIN right")
                win = 1
                return win


def is_win(board, size, turn):
    if col_win(size, turn, board) == 1:
        return 1
    elif row_win(size, turn, board) == 1:
        return 1
    elif diag_win(size, board, turn) == 1:
        return 1


def valid_size():
    size = input("how big ?")
    # worked with == False
    while not size.isdigit() or int(size) <= 2:
        size = input("has to be a number bigger then 2 - ")
    size = int(size)
    return size


def valid_num(num_check, size: int) -> int:
    # worked with == False
    while not num_check.isdigit() or 0 >= int(num_check) or int(num_check) > size ** 2:
        num_check = (input('has to be a number between 1 to -' + str(size ** 2)))
    num_check = int(num_check)
    return num_check


# noinspection SpellCheckingInspection
def valid_slot(board: list, size: int):
    num = (input("where do you want to play?-"))
    validnum = valid_num(num, size)
    validnum = int(validnum) - 1
    while board[validnum] == '|_🐕_|' or board[validnum] == '|_🐈_|':
        num = input("cant pick a taken slot-")
        validnum = valid_num(num, size)
        validnum = int(validnum) - 1
    return validnum


# noinspection PyPep8Naming
def X_Y(p1counter: int, p2counter: int):
    if p1counter > p2counter:
        return '🐕'
    elif p2counter == p1counter:
        return '🐈'
    #
    # turn_1 = input("X OR Y")
    # turn_1 = str(turn_1).upper()
    # while turn_1 != 'X' and p2counter != p1counter or turn_1 != 'Y' and p2counter == p1counter:
    #     if turn_1 != 'X' and turn_1 != 'Y':
    #         turn_1 = input("has to be X OR Y")
    #         turn_1 = str(turn_1).upper()
    #     elif p1counter > p2counter and turn_1 != 'X':
    #         turn_1 = input("has to be X for" + player1)
    #         turn_1 = str(turn_1).upper()
    #     elif p2counter == p1counter and turn_1 != 'Y':
    #         turn_1 = input("has to be Y for" + player2)
    #         turn_1 = str(turn_1).upper()
    #     else:
    #         return turn_1
    # return turn_1


def game_stuck(board: list):
    if '|___|' not in board:
        win = 1
        print("game is stuck, no winner")
        return win


def new_game():
    size = valid_size()
    print(type(size))
    turn = [0, ' 1']
    board = board_updated(size, turn)
    board_printer(size, board)
    win = 0
    player1 = input("player one -")
    player2 = input("player two -")
    p1counter = 0
    p2counter = 0
    print([board[(size+2*z)-1] for z in range(0, size)])
    while win != 1:
        if p2counter == p1counter:
            p1counter += 1
            print(player1+'🐕' + "'s turn")
        else:
            print(player2 + '🐈' "'s turn")
            p2counter += 1
        turn[0] = valid_slot(board, size)
        turn[1] = X_Y(p1counter, p2counter)
        board[turn[0]] = ('|_' + turn[1] + '_|')
        board_printer(size, board)
        win = is_win(board, size, turn)
    if p2counter == p1counter:
        return print(player1 + '🐕' + "WON")
    else:
        return print(player2 + '🐈' "WON")

new_game()
