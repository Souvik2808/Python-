
# Python Program to Shuffle Deck of Cards

import random

suits = ['Hearts','Diamonds','Clubs','Spades']
ranks = ['1','2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

# Create Deck......

deck = [f'{rank} of {suit}' for suit in suits for rank in ranks]

# Randomly Shuffle deck of card....

random.shuffle(deck)

print("Shuffle Deck of Cards ......")
for card in deck:
    print(card)