# Main Entry Point for the Baccarat Application
# Baccarat
# This project will allow the user to enter the number of decks to be used in the "sleeve" before reshuffling
# Clubs : CA CK CQ CJ C10 C9 C8 C7 C6 C5 C4 C3 C2
# Spades : SA SK SQ SJ S10 S9 S8 S7 S6 S5 S4 S3 S2
# Hearts : HA HK HQ HJ H10 H9 H8 H7 H6 H5 H4 H3 H2
# Diamonds : DA DK DQ DJ D10 D9 D8 D7 D6 D5 D4 D3 D2

import random

numberOfDecks = input("Enter the number of decks to use: ")
clubs   = ['CA', 'CK', 'CQ', 'CJ', 'C10', 'C9', 'C8', 'C7', 'C6', 'C5', 'C4', 'C3', 'C2']
spades  = ['SA', 'SK', 'SQ', 'SJ', 'S10', 'S9', 'S8', 'S7', 'S6', 'S5', 'S4', 'S3', 'S2']
hearts  = ['HA', 'HK', 'HQ', 'HJ', 'H10', 'H9', 'H8', 'H7', 'H6', 'H5', 'H4', 'H3', 'H2']
diamonds= ['DA', 'DK', 'DQ', 'DJ', 'D10', 'D9', 'D8', 'D7', 'D6', 'D5', 'D4', 'D3', 'D2']
deck = []
for num in range(numberOfDecks):
    deck.extend(clubs)
    deck.extend(spades)
    deck.extend(hearts)
    deck.extend(diamonds)
random.shuffle(deck)
print deck
print len(deck)

i=0

for i in range(0, 12, 4):
    print deck[i], deck[i+2]
    print deck[i+1], deck[i+3]
    print "---------------------"

player=[deck[i], deck[i+2]];
#banker=[deck[i+1], deck[i+4]];