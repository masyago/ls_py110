import random
import os

FIRST_MOVE = 'Computer' # Options are 'Computer', 'Player', 'Choose'
INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = '0'
SCORE_TO_WIN = 1
WINNING_LINES = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9], # columns
    [1, 5, 9], [3, 5, 7]             # diagonals
        ]

END_GAME = ['n', 'no']
DONT_END_GAME = ['y', 'yes']

def display_welcome_massage():
    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}")

def display_board(board):
    # os.system('clear')
    
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

def join_or(valid_choices, delimiter=', ', conjunction='or'):
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

def find_at_risk_square(line, board, marker):
    markers_in_line = [board[square] for square in line]

    if markers_in_line.count(marker) == 2:
        for square in line:
            if board[square] == INITIAL_MARKER:
                return square
            
    return None

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    
    square = None
    if board[5] == INITIAL_MARKER:
        square = 5
    else:
        for line in WINNING_LINES:
            square = find_at_risk_square(line, board, COMPUTER_MARKER)
            if square:
                break
        
        if not square:
            for line in WINNING_LINES:
                square = find_at_risk_square(line, board, HUMAN_MARKER)
                if square:
                    break

        if not square:
            square = random.choice(empty_squares(board))

    board[square] = COMPUTER_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def detect_winner(board):
    
    for line in WINNING_LINES:
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
    1 : ' ', # top left
    2 : ' ', # top center
    3 : ' ', # top right
    4 : ' ', # middle left
    5 : ' ', # middle center
    6 : ' ', # middle right
    7 : ' ', # bottom left
    8 : ' ', # bottom center
    9 : ' ' # bottom right
}


def play_tic_tac_toe():
    while True:
        score = {
        'Player' : 0,
        'Computer' : 0
        }

        if FIRST_MOVE == 'Choose':
            who_starts = input('Who should go first? Player (p) or computer (c)\n')
        else:
            who_starts = FIRST_MOVE
            prompt(f'{who_starts} goes first.')
        
        while True:
            board = initialize_board()
            display_welcome_massage()
            display_board(board)

            while True:

                # display_board(board)

                if who_starts[0].lower() == 'p':
                    player_chooses_square(board)
                    display_board(board)
                    if someone_won(board) or board_full(board):
                        break

                    computer_chooses_square(board)
                    display_board(board)
                    if someone_won(board) or board_full(board):
                        break

                elif who_starts[0].lower() == 'c':
                    computer_chooses_square(board)
                    display_board(board)
                    if someone_won(board) or board_full(board):
                        break
                
                    player_chooses_square(board)
                    display_board(board)
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
        # answer = input().lower()

        while True:
            answer = input().lower()
            
            if answer.lower().strip() in (END_GAME + DONT_END_GAME):
                break

            prompt("It's not a valid answer. Try again. ")
            
            
        if answer.lower().strip() in END_GAME:
            break

    prompt('Thanks for playing Tic Tac Toe!')

play_tic_tac_toe()

