import random

SUITS = ('H', 'D', 'S', 'C')
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
TARGET_TOTAL_CARD_SCORE = 21
SCORE_TO_WIN = 3

def prompt(message):
    print(f"\n=> {message}")

def initialize_deck():
    deck = [f"{value}{suit}" for value in VALUES for suit in SUITS]
    random.shuffle(deck)
    return deck

def total(cards):
    sum_val = 0

    for card in cards:
        value = card[:-1]

        if value == "A":
            sum_val += 11
        elif value in ['J', 'Q', 'K']:
            sum_val += 10
        else:
            sum_val += int(value)

    # Correct for Aces
    for card in cards:
        value = card[:-1]
        if sum_val <= TARGET_TOTAL_CARD_SCORE:
            break
        if value == "A":
            sum_val -= 10

    return sum_val

def busted(cards_total):
    return cards_total > TARGET_TOTAL_CARD_SCORE

def detect_result(dealer_total, player_total):
    if player_total > TARGET_TOTAL_CARD_SCORE:
        return 'PLAYER_BUSTED'
    elif dealer_total > TARGET_TOTAL_CARD_SCORE:
        return 'DEALER_BUSTED'
    elif dealer_total < player_total:
        return 'PLAYER'
    elif dealer_total > player_total:
        return 'DEALER'
    else:
        return 'TIE'

def display_results(dealer_total, player_total):
    result = detect_result(dealer_total, player_total)

    if result == 'PLAYER_BUSTED':
        prompt('You busted! Dealer wins!')
    elif result == 'DEALER_BUSTED':
        prompt('Dealer busted! You win!')
    elif result == 'PLAYER':
        prompt('You win!')
    elif result == 'DEALER':
        prompt('Dealer wins!')
    else:
        prompt("It's a tie!")

def keep_score(dealer_total, player_total):
    result = detect_result(dealer_total, player_total)

    if result in ['PLAYER', 'DEALER_BUSTED']:
        score['PLAYER'] += 1
    elif result in ['DEALER', 'PLAYER_BUSTED']:
        score['DEALER'] += 1

def display_score(score):
    prompt(f"Current score\nPLAYER {score['PLAYER']} : DEALER {score['DEALER']}")

def game_winner(score):
    if score['PLAYER'] == SCORE_TO_WIN or score['DEALER'] == SCORE_TO_WIN:
        return True


def display_game_winner(score):
    if score['PLAYER'] == SCORE_TO_WIN:
        prompt(f"Player won the game with the score PLAYER {score['PLAYER']} : DEALER {score['DEALER']}")
    elif score['DEALER'] == SCORE_TO_WIN:
        prompt(f"Dealer won the game with the score PLAYER {score['PLAYER']} : DEALER {score['DEALER']}")


def play_again():
    print("-------------")
    answer = input('Do you want to play again? (y or n) ')
    return answer == 'y'

def pop_two_from_deck(deck):
    return [deck.pop(), deck.pop()]

def hand(cards):
    return ', '.join(cards)

while True:
    prompt('Welcome to Twenty-One!')

    score = {'PLAYER' : 0,
                'DEALER' : 0
                }

    while True:
        
        
        # initial deal
        deck = initialize_deck()
        player_cards = pop_two_from_deck(deck)
        dealer_cards = pop_two_from_deck(deck)

        player_total = total(player_cards)
        dealer_total = total(dealer_cards)


        prompt(f"Dealer has {dealer_cards[0]} and ?")
        prompt(f"You have: {player_cards[0]} and {player_cards[1]}, for a total of {player_total}.")

        # player turn
        while True:
            player_choice = input("\nWould you like to (h)it or (s)tay? ")
            if player_choice not in ['h', 's']:
                prompt("Sorry, must enter 'h' or 's'.")
                continue

            if player_choice == 'h':
                player_cards.append(deck.pop())
                player_total = total(player_cards)

                prompt('You chose to hit!')
                prompt(f"Your cards are now: {hand(player_cards)}")
                prompt(f"Your total is now: {total(player_cards)}")

            if player_choice == 's' or busted(player_total):
                break

        if busted(player_total):
            display_results(dealer_total, player_total)
            score['DEALER'] += 1
            display_score(score)
            break
        
        # if game_winner(score):
        #         display_game_winner(score)
        #         break

            # if play_again():
            #     continue
        else:
            prompt(f"You stayed at {player_total}")

        # dealer turn
        prompt("Dealer's turn...")

        while dealer_total < 17:
            prompt("Dealer hits!")
            dealer_cards.append(deck.pop())
            dealer_total = total(dealer_cards)
            prompt(f"Dealer's cards are now: {hand(dealer_cards)}")

        if busted(dealer_total):
            prompt(f"Dealer total is now: {total(dealer_cards)}")
            display_results(dealer_total, player_total)
            score['PLAYER'] += 1
            display_score(score)
            break
        # if game_winner(score):
        #     display_game_winner(score)
        #     break
            # if play_again():
            #     continue
        else:
            prompt(f"Dealer stays at {dealer_total}")

        # both player and dealer stays - compare cards!

        if not (busted(player_total) or busted(dealer_total)): 
            print('==============')
            prompt(f"Dealer has {hand(dealer_cards)}, for a total of: {dealer_total}")
            prompt(f"Player has {hand(player_cards)}, for a total of: {player_total}")
            print('==============')

            display_results(dealer_total, player_total)
            keep_score(dealer_total, player_total)
            display_score(score)
            display_game_winner(score)

        if game_winner(score):
            display_game_winner(score)
            break

    if not play_again():
        break