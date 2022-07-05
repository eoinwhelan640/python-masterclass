import random

card_values = {
    'K':10,
    'Q':10,
    'J':10,
    'A':None
}

for i in range(2,11):
    card_values[str(i)] = i
print(card_values)


# play blackjack
# def deal_card(n):
#     '''Deal n number of cards'''
#     cards = random.choices(list(card_values), k=n)
#     value = 0
#     for card in cards:
#         value += int(card_values[card])
#     return cards, value
#
#
#
# while True:
#     input("Press Enter to play Blackjack: ")
#     dealer_cards, dealer_value = deal_card(1)
#     player_cards, player_value = deal_card(1)
#     # print(f'Player Hand is {player_cards} ({player_value})')
#     # print(f'Dealer Hand is {dealer_cards} ({dealer_value})')
#     # play = input('Hit/Stick or quit: ').casefold()
#     play='hit'
#     while True:
#         if play == 'quit':
#             break
#         if play == 'hit':
#             player_hit_card, player_hit_value = deal_card(1)
#             player_value += player_hit_value
#             [player_cards.append(c) for c in player_hit_card]
#         if dealer_value < 17:
#             print('Dealer hits')
#             dealer_hit_card, dealer_hit_value = deal_card(1)
#             dealer_value += dealer_hit_value
#             [dealer_cards.append(c) for c in dealer_hit_card]
#         if player_value > 21:
#             print('PLAYER BUST ')
#             break
#         if dealer_value > 21:
#             print('DEALER BUST')
#             break
#         if play == 'stick' and dealer_value >= 17:
#             break
#         print(f"Player hand is {player_cards} ({player_value})")
#         print(f"Dealer hand is {dealer_cards} ({dealer_value})")
#         play = input('Hit/Stick or quit: ').casefold()
#     if play =='quit':
#         print('Exiting...')
#         break
#     if player_value > dealer_value and player_value <= 21:
#         print(f'PLAYER BEAT DEALER')
#     elif player_value <= dealer_value and dealer_value <= 21:
#         print(f'DEALER BEAT PLAYER')
#     print(f'PLAYER {player_cards} ({player_value}) vs DEALER {dealer_cards} ({dealer_value})')








# Parts of the game
# Deal two cards (apply to player + dealer)
# Choose hit or stick
# Deal one card
# Dealer sticks on 17
# Whoever is higher wins

# try again
def deal_card(n):
    '''Deal n number of cards'''
    return random.choices(list(card_values), k=n)

def play_round(dealer_cards,player_cards):
    player_choice = input("Hit or stick: ").casefold()
    if player_choice=='quit':
        return None,None
    dealer_value = get_hand_value(dealer_cards)
    if dealer_value < 17:
        [dealer_cards.append(c) for c in deal_card(1)]
    if player_choice == 'hit':
        [player_cards.append(c) for c in deal_card(1)]
    [print_hand_value(p,h) for p,h in zip(["Dealer","Player"], [dealer_cards,player_cards])]
    return dealer_cards,player_cards

def get_hand_value(cards):
    value = 0
    aces = cards.count('A')
    for card in cards:
        if card != 'A':
            value += int(card_values[card])
    for ace in range(aces):
        print(f"{cards} ({value + 1})")
        print(f"{cards} ({value + 11})")
        choice = input("Choose value for Ace, 1 or 11: ")
        value += int(choice)
    return value
def print_hand_value(user,cards):
    print(f"{user} hand {cards} ({get_hand_value(cards)})")
def evaluate_winner(dealer,player):
    if (dealer <= 21) & (player <= 21):
        if dealer >= player:
            return "Dealer"
        else:
            return "Player"
    elif (dealer >= 21) & (player >= 21):
        print("Dealer & Player Bust")
        return "Player"
    elif dealer > 21:
        print('Dealer BUST')
        return "Player"
    else:
        print('Player BUST')
        return "Dealer"
def play_blackjack():
    while True:
        input("Press Enter to play Blackjack>: ")
        dealer = deal_card(2)
        player = deal_card(2)
        [print_hand_value(p,h) for p,h in zip(["Dealer","Player"], [dealer,player])]
        dealer_hand, dealer_value, player_hand,player_value = run_round(dealer,player)
        if dealer_hand == None:
            break
        winner = evaluate_winner(dealer_value, player_value)
        print(f"{winner} WINS")
# The hard functions
def run_round(dealer, player):
    last_dealer_value = get_hand_value(dealer)
    last_player_value = get_hand_value(player)
    while True:
        # Play a round of hit/stick
        play_round(dealer, player)
        if player == None:
            print('Exiting...')
            return None,None,None,None
        # Find vals of current hands
        dealer_value = get_hand_value(dealer)
        player_value = get_hand_value(player)

        if player_value > 21:
            break
        if dealer_value > 21:
            break
        if (last_player_value == player_value) & (last_dealer_value == dealer_value):
            break
        last_player_value = player_value
        last_dealer_value = dealer_value
    return dealer, dealer_value, player, player_value
#run_round(['K','10'], ['9','3'])
play_blackjack()

#print(get_hand_value(['6','5']))
#print(f"output value is {get_hand_value(['3','A'])}")
#print(get_hand_value(['A','10']))
#print(get_hand_value(['A','A']))


# Fix this
