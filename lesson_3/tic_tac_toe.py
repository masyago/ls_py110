import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = '0'
SCORE_TO_WIN = 5

def display_board(board):
    # os.system('clear')
    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}")

    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  | {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  | {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  | {board[9]}")
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def prompt(message):
    print(f'==> {message}')

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def join_or(valid_choices, delimiter=', ', conjunction='or'): # From a list, output 1, 2, or 3.
    valid_choices_str = [str(num) for num in valid_choices]
    if not valid_choices_str:
        return ''
    elif len(valid_choices_str) == 1:
        return str(valid_choices_str[0])
    elif len(valid_choices_str) == 2:
        return f"{str(valid_choices_str[0])}{delimiter}{str(valid_choices_str[1])}"
    else: 
        return f"{delimiter.join(valid_choices_str[:-1])}{delimiter}{conjunction} {valid_choices_str[-1]}"

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices)}): ")
        square = input().strip()
        if square in valid_choices:
            break
        
        prompt("Not a valid number.")

    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9], # columns
        [1, 5, 9], [3, 5, 7]             # diagonals
            ]
    
    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER 
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):
            return 'Computer'
        
    return None


def someone_won(board):
    return bool(detect_winner(board))

def keep_score(score):
    # while all(value < SCORE_TO_WIN for value in score.values()):
    if detect_winner(board) == 'Player':
        score['Player'] += 1
    elif detect_winner(board) == 'Computer':
        score['Computer'] += 1

    print(score)

def display_score(score):
    prompt(f"Current score is {score['Player']} : {score['Computer']}")




board = {
    1 : 'X', # top left
    2 : ' ', # top center
    3 : ' ', # top right
    4 : ' ', # middle left
    5 : 'O', # middle center
    6 : ' ', # middle right
    7 : ' ', # bottom left
    8 : ' ', # bottom center
    9 : 'X' # bottom right
}


def play_tic_tac_toe():
    while True:
        score = {
        'Player' : 0,
        'Computer' : 0
        }
        
        while True:
            board = initialize_board()

            while True:
                display_board(board)

                player_chooses_square(board)
                if someone_won(board) or board_full(board):
                    break

                computer_chooses_square(board)
                if someone_won(board) or board_full(board):
                    break

            if someone_won(board):
                prompt(f"{detect_winner(board)} won!")
            else:
                prompt(f"It's a tie!")

            if detect_winner(board) == 'Player':
                score['Player'] += 1
            elif detect_winner(board) == 'Computer':
                score['Computer'] += 1

            prompt(f"SCORE Player {score['Player']} : Computer {score['Computer']}")

            if score['Player'] == SCORE_TO_WIN:
                prompt(f'You won the game. Congratulations!')
                break
            elif score['Computer'] == SCORE_TO_WIN:
                prompt('Computer won the game!')
                break
            
    
        prompt('Play agan? (y or n)')
        answer = input().lower()

        if answer[0] != 'y':
            break

    prompt('Thanks for playing Tic Tac Toe!')

play_tic_tac_toe()

