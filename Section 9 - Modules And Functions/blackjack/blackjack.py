# Blackjack would have been eaiser to do it in format
# Deal 2 cards to everyone
# player takes all their goes
# Dealer takes his goes
# result
# my way on my_blackjack was very overcomplicated, no need to bind players together
# plus that made it impossible to add more poeple into the game
import tkinter as tk
import random
# Loading the card images
# We've labbeled the individual images as <number>_<suit>.<extension> to make accessing them much easier from within
# functions
def load_images(card_images):
    suits = ['heart','club','diamond','spade']
    face_cards = ['jack','queen','king']
    if tk.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    # for each suit retrieve the image for the cards
    for suit in suits:
        # treating Ace as 1.
        for card in range(1,11):
            name = f"cards_{extension}/{str(card)}_{suit}.{extension}"
            image = tk.PhotoImage(file=name)
            card_images.append((card,image,))
        # Next the face cards
        for card in face_cards:
            name = f"cards_{extension}/{str(card)}_{suit}.{extension}"
            image = tk.PhotoImage(file=name)
            card_images.append((10, image))


def _deal_card(frame):
    # pop the next card off the top of the deck - 0 gives first
    next_card = deck.pop(0)
    # and add that card to bottom of deck
    deck.append(next_card)
    # add the image to a label and display the label
    # we use pack over grid, pack is much simpler, as we add new ones to left they just stack against ones already there
    # As a rule, dont mix grid and pack in windows, but cos each widget is a window, packing images into the frame
    # is fine as long as we dont try anyything else with grid
    tk.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # now return the cards face value
    return next_card

# create two functions for dealing cards
def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(_deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins! ")
    elif dealer_score > 21 or dealer_score< player_score:
        result_text.set("Player wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer wins")
    else:
        result_text.set("Draw")


def score_hand(hand):
    '''Calculate the total score of all cards in the list'''
    # only one ace can have value 11, this is reduced to 1 if hand would bust
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_player():
    player_hand.append(_deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer wins!")


# Using globals, don't do it this way!!
# def deal_player():
#     global player_score
#     global player_ace
#     card_value = deal_card(player_card_frame)[0]
#     if card_value == 1 and not player_ace:
#         player_ace = True
#         card_value = 11
#     player_score += card_value
#     # If we would bust, check if theres an ace and subtract 10
#     if player_score > 21 and player_ace:
#         player_score -= 10
#         player_ace = False
#     player_score_label.set(player_score)
#     if player_score > 21:
#         result_text.set("Dealer wins!")


# Dont need to set up a whole new GUI everytime, just reset the Frames
# Probably dont need global keyword here, think this makes it work with python2
def initial_deal():
    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    # embedded frame to hold the card images
    dealer_card_frame.destroy()
    dealer_card_frame = tk.Frame(card_frame, background='green')
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)
    # embedded frame to hold card images
    player_card_frame = tk.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    result_text.set("")
    dealer_hand = []
    player_hand = []
    initial_deal()


def shuffle():
    random.shuffle(deck)


def play_blackjack():
    initial_deal()
    mainWindow.mainloop()



mainWindow = tk.Tk()

mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(background='green')


result_text = tk.StringVar()
result = tk.Label(mainWindow, textvariable= result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tk.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)


dealer_score_label = tk.IntVar()
tk.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tk.Label(card_frame, textvariable=dealer_score_label, background="green", fg='white').grid(row=1, column=0)


# Embedded frame to hold the card images
dealer_card_frame = tk.Frame(card_frame, background='green')
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tk.IntVar()
tk.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tk.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3,column=0)

# embedded frame to hold the card images
player_card_frame = tk.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)


button_frame = tk.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

## link the dealing functions within this button we've created
dealer_button = tk.Button(button_frame, text='Dealer', command=deal_dealer)
dealer_button.grid(row=0, column=0)


player_button = tk.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

# New button for restarting game
new_game_button = tk.Button(button_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column = 2)

# Add a button to shuffle the deck
shuffle_button = tk.Button(button_frame, text="Shuffle", command= shuffle)
shuffle_button.grid(row=0, column=3)

cards = []
load_images(cards)
print(cards)

# create a new deck of cards and shuffle them
deck = list(cards)
# If you wanted to play with 3 decks
#deck = list(cards) + list(cards) + list(cards)
shuffle()

# Create the list to store dealers and players hands
dealer_hand = []
player_hand = []


if __name__ == '__main__':
    play_blackjack()
