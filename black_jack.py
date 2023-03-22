import os, random, string, math

Ace=1
J=Q=K=10
deck = []

# Intro
print ("Welcome to Blackjack simulation, where we will test how often we bust based on predetermined policies!\n")

def infDeckGame():
    print ("You have chosen an infinite deck!\n")
def stanDeckGame():
    print ("You have chosen a standard deck!\n")

def startGame():
    decktype = 0
    _ace = 0
    global Ace  # needs to be defined here as global to change value of variable


    #Player chooses whether Ace's value is 1 or 10
    _ace = input("Select value of Ace, Choose [0] for a value of 1 or [1] for a value of 10 \n")
    if _ace == "0":
        Ace = 1
        print("A is now ", Ace)
    elif _ace == "1":
        Ace = 10
        print("A is now ", Ace)
    else:
        print("Incorrect input, Ace value will be defaulted to 1")
    


    decktype = input( "Choose a deck type [I]nfinite or [S]tandard: \n")
    if decktype == "I" or decktype == "i":
        infDeckGame()
        #exit()
    elif decktype == "S" or decktype == "s":
        stanDeckGame()
        #exit()
    else:
        print("Incorrect input! Ending simulation!")
        exit()

# Change settings prompt
settings = input("Do you want to change settings[Y]? Default: Ace=1, No card replacement \n")
if settings == "Y" or settings == "y":
    startGame()

# Create deck after settings
deck = [Ace,2,3,4,5,6,7,8,9,10,J,Q,K]*4

# Random  index
pick1 = random.randint(0,len(deck)-1)
pick2 = random.randint(0,len(deck)-1)

# Select card based on index
card1 = deck[pick1]
card2 = deck[pick2]

print(card1, card2)
print("your sum is: ", card1+card2)