import os, random, string, math, time

Ace=1
J=Q=K=10
deck = []
hard = True
standard = False
sumTotal = 0
policy = 1

# Intro
print ("Welcome to Blackjack simulation, where we will test how often we bust based on predetermined policies!\n")

def infDeckGame():
    print ("You have chosen an infinite deck!\n")
    global standard
    standard = False
def stanDeckGame():
    print ("You have chosen a standard deck!\n")
    global standard
    standard = True

def startGame():
    decktype = 0
    _ace = 0
    global Ace  # needs to be defined here as global to change value of variable


    #Player chooses whether Ace's value is 1 or 11
    _ace = input("Select value of Ace, Choose [0] for a value of 1 or [1] for a value of 10 \n")
    if _ace == "0":
        Ace = 1
        print("A is now ", Ace)
    elif _ace == "1":
        Ace = 11
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

# POLICY
def _PolicySelected(x):
    # POLICY 1
    if x == 1:
        if sumTotal>=17: 
            print("stick, Policy 1")
        elif sumTotal<17:
            print("hit, Policy 1")
            while sumTotal < 21:
                hit()
    # POLICY 2
    elif x == 2:
        if sumTotal>=17 and hard: 
            print("stick, Policy 2")
        elif sumTotal<17 and hard:
            print("hit, Policy 2")
            while sumTotal < 21:
                hit()
    # POLICY 3
    elif x == 3: 
        print("stick, Policy 3")
    # POLICY 4
    elif x == 4:
        print("hit, Policy 4")
        while sumTotal < 21:
                hit()
    # POLICY 5


# Change settings prompt
settings = input("Do you want to change settings[Y]? Default: Ace=1, No card replacement \n")
if settings == "Y" or settings == "y":
    startGame()


# CHECK IF 21 OR OVER
def check():
    if sumTotal==21:
        print("21! You win")
    elif sumTotal > 21:
        print("Bust! You went over 21")

# HIT
def hit():
    global sumTotal
    pick = random.randint(0,len(deck)-1)
    card = deck[pick]

    # HARD IF ACE IS NOT IN HAND, SOFT IF ACE IS IN HAND
    if card == Ace or card == Ace:
        hard = False
        print("Drew an ace: ", Ace)
    else:
        hard = True
        #print("hard \n")

    if standard:
        del deck[pick]
    sumTotal += card
    print("After Hit:", sumTotal, " Deck:", len(deck))
    check()

# DEAL CARDS
def deal(user):
    print(user, "\n")
    global sumTotal
    global deck
    # Random  index for player
    pick1 = random.randint(0,len(deck)-1)
    pick2 = random.randint(0,len(deck)-1)


    # Select card based on index for player
    card1 = deck[pick1]
    card2 = deck[pick2]

    # REMOVE CARDS FROM DECK
    if standard:
        del deck[pick1]
        del deck[pick2]
        print(len(deck))

    # HARD IF ACE IS NOT IN HAND, SOFT IF ACE IS IN HAND
    if card1 == Ace or card2== Ace:
        hard = False
        print("Drew an ace: ", Ace)
    else:
        hard = True
        #print("hard \n")

    print("Card 1:", card1)
    print("Card 2:", card2)
    print("your sum is: ", card1+card2)

    sumTotal = card1+card2
    check() #CHECK WIN/BUST BEFORE HITTING
    _PolicySelected(policy)
    


rounds = int(input("Enter a number of rounds \n"))
policy = int(input("Select a policy to play. 1,2,3,4,5"))
print(policy)
x = 1

while x<=rounds:
    # Create deck and shuffle deck after settings
    deck = [Ace,2,3,4,5,6,7,8,9,10,J,Q,K]*4
    random.shuffle(deck)
    print("\n---------------------------------------")
    print("Round: ", x)
    deal("Player 1")
    print("\n")
    deal("Player 2")
    x += 1
    time.sleep(.2)
