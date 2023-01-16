def print_greeting():
    """
    The functions prints greeting to the users at the beginning
    of the game
    """
    pass


def get_board_size():
    """
    Get board size from the input including validations
    """
    pass


def initialize_board():
    """
    Initialize the game board according to the board size
    received from the user
    """
    pass


def display_current_board():
    """
    Display current game board in a user-friendly way
    """
    pass


def display_turn_prompt():
    """
    Ask relevant player to insert his move.
    Consider the best way to display the board to the user
    and how the user should indicate where he wants to put X or O
    """
    pass


def get_user_turn():
    """
    Receive user's move including validations
    """
    pass


def update_board_with_turn():
    """
    Update game board with new user turn
    """
    pass


def no_moves_left():
    """
    Check whether the game is finished (no more moves left - the board is full)
    """
    pass


def has_winner():
    """
    Check whether there is a winner.
    This function should use the following functions to detect
    whether there is a winner:
    row_wins()
    column_wins()
    diagonal_wins()
    """
    pass


def row_wins():
    """
    Check whether there is a winner in a row
    """
    pass


def column_wins():
    """
    Check whether there is a winner in a column
    """
    pass


def diagonal_wins():
    """
    Check whether there is a winner in one of teo diagonals
    :return:
    """
    pass


#bonus
def game_stuck():
    """
    Bonus: check whether the game is stuck (it is useless to
    continue a game if no one can win - the board is not full,
    but every row, column, and diagonal is filled both with X and O)
    """
    pass

### FUNCTIONS ###

# greetings
# input_board_size -> User choose
# initialize_board -> How it stores the data
# draw_current_board
# change_player_turn
# input_valid_move
# update_board -> {different from # draw_current_board}
# result -> Announce if there is a winner and who won

### CHECK ###

# is_end_of_game
# is_win ->
# {depends on type of how you store the board}
# - One of the line wins
# - One of the columns win
# - One of the diagonals win
#
# # is_draw ->
# Draw when all lines & columns & diagonals consists at least
# with one 'X' and at least with one '0'
#
# ### PROGRAMM ###
#
# >> initialization
#
# start game
# >> get_input
# >> update_board
# >> draw_current_board
# >> check if is_end_of_game
# >> result