# AI defense
# Computer will try to defend the third square when 2 in a row a
# taken by player
INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = '0'
SCORE_TO_WIN = 5

WINNING_LINES = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9], # columns
    [1, 5, 9], [3, 5, 7]             # diagonals
        ]

board = {
    1 : 'X', # top left
    2 : 'X', # top center
    3 : ' ', # top right
    4 : ' ', # middle left
    5 : ' ', # middle center
    6 : ' ', # middle right
    7 : ' ', # bottom left
    8 : ' ', # bottom center
    9 : ' ' # bottom right
}


# def detect_winner(board):
    
#     for line in WINNING_LINES:
#         sq1, sq2, sq3 = line
#         if (board[sq1] == HUMAN_MARKER 
#                 and board[sq2] == HUMAN_MARKER
#                 and board[sq3] == HUMAN_MARKER):
#             return 'Player'
#         elif (board[sq1] == COMPUTER_MARKER
#                 and board[sq2] == COMPUTER_MARKER
#                 and board[sq3] == COMPUTER_MARKER):
#             return 'Computer'
        
#     return None

def computer_defense(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER and board[sq2] == HUMAN_MARKER):
            board[sq3] = COMPUTER_MARKER
        elif (board[sq2] == HUMAN_MARKER and board[sq3] == HUMAN_MARKER):
            board[sq1] = COMPUTER_MARKER
        elif (board[sq1] == HUMAN_MARKER and board[sq3] == HUMAN_MARKER):
            board[sq2] = COMPUTER_MARKER

    return board

print(computer_defense(board))