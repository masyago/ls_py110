# 1. Initialize deck - DONE
# 2. Deal cards to player and dealer - DONE
# 3. Player turn: hit or stay - DONE
#    - repeat until bust or stay - DONE
# 4. If player bust, dealer wins. - DONE
# 5. Dealer turn: hit or stay -DONE
#    - repeat until total >= 17 
# 6. If dealer busts, player wins. - 
# 7. Compare cards and declare winner.

import random

# Deck of cards: list of sublists. Sublist: ['suit', 'value']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITES = ['C', 'D', 'H', 'S']
TWENTY_ONE = 21

def initialize_deck():
    return [[suit, value] for suit in SUITES
                          for value in VALUES]

def shuffle(deck):
    random.shuffle(deck)

def deal_cards(deck):
    for _ in range(2):
        player_cards.append(deck.pop())
        dealer_cards.append(deck.pop())

def deal_one_more_card(deck, person):
    if person == 'Player':
        player_cards.append(deck.pop())
    elif person == 'Dealer':
        dealer_cards.append(deck.pop())

    return deck


def sum_value(cards):
    values = [card[1] for card in cards]

    total_value = 0
    for value in values:
        if value == 'A':
            total_value += 11
        elif value in ['J', 'Q', 'K']:
            total_value += 10
        else:
            total_value += int(value)

    # Aces value correction
    aces = values.count('A')
    while total_value > TWENTY_ONE and aces:
        total_value -= 10
        aces -= 1

    return total_value

def busted(total_value):
    if total_value > TWENTY_ONE:
        return True
    
    return False

def display_winner(person):
    if person == 'Dealer':
        print('Dealer won the game.')
    elif person == 'Player':
        print('You won the game. Congratulations!')
    elif person == 'Nobody':
        print("It's a tie.")

def determine_winner(player_sum_value, dealer_sum_value):
    if ((player_sum_value <= TWENTY_ONE) and (player_sum_value > dealer_sum_value)):
        return 'Player'
    elif ((dealer_sum_value <= TWENTY_ONE) and (dealer_sum_value > player_sum_value)): 
        return 'Dealer'
    else:
        return 'Nobody'

    
player_cards = [] # not sure if they the variables should be global
dealer_cards = [] # not sure if they the variables should be global


def play_21():
    deck = initialize_deck()
    shuffle(deck)
    deal_cards(deck)
    print(f"Player cards: {player_cards}. ")
    print(f"One of the dealer cards: {random.choice(dealer_cards)}")
    player_sum_value = sum_value(player_cards)
    dealer_sum_value = sum_value(dealer_cards)

    # print(player_sum_value)
    # print(dealer_sum_value) # update to show only one dealer's card

    # Player turn
    while True:
        answer = input("\nhit or stay? ")
        if answer == 'stay':
            break
        elif answer == 'hit':
            deal_one_more_card(deck, 'Player')
            print(f'\nYour cards are {player_cards}')
            player_sum_value = sum_value(player_cards)

        # print(f"Player sum: {player_sum_value}")
        # print(busted(player_sum_value))
        if busted(player_sum_value):
            break
            

    if busted(player_sum_value):
        print(player_cards)
        print('\nBusted! Value is more than 21!')
        display_winner('Dealer')
    else:
        print('\nYou chose to stay!')

        while dealer_sum_value < 17:
            deal_one_more_card(deck, 'Dealer')
            dealer_sum_value = sum_value(dealer_cards)
            print(dealer_cards)


        if busted(dealer_sum_value):
            print('\nDealer is busted. You won!')
        else:
            print('\nDealer chose to stay')
            print(f"\nFinal player cards: {player_cards}")
            print(f"Final dealer cards: {dealer_cards}")

            print(f'Player sum: {player_sum_value}')
            print(f'Dealer sum: {dealer_sum_value}')

            display_winner(determine_winner(player_sum_value, dealer_sum_value))



play_21()