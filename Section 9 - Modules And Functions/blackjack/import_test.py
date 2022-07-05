import blackjack
# If do the below, things starting with _ wont be imported, python knows the convention of using _ to make them private
from blackjack import *
# Dont need to do .copy() when we do sorted, cos that also takes a copy
g = sorted(globals())  #.copy()
for x in g:
    print(x)


# print(__name__)
# blackjack._deal_card(blackjack.dealer_card_frame)
# blackjack.play_blackjack()
# from a command line
#python -m blackjack