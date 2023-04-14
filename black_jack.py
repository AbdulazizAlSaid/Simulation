import os
import random
import string
import math
import time
import numpy as np
import matplotlib.pyplot as plt
import statistics as st

Ace = 1
J = Q = K = 10
deck = []
hard = True
standard = False
sumTotal = 0
policy = 1
totalWin = 0
p1Value = 0

# Intro
print("Welcome to Blackjack simulation, where we will test how often we bust based on predetermined policies!\n")


def infDeckGame():
    print("You have chosen an infinite deck!\n")
    global standard
    standard = False


def stanDeckGame():
    print("You have chosen a standard deck!\n")
    global standard
    standard = True


def startGame():
    decktype = 0
    _ace = 0
    global Ace  # needs to be defined here as global to change value of variable

    # Player chooses whether Ace's value is 1 or 11
    _ace = input(
        "Select value of Ace, Choose [0] for a value of 1 or [1] for a value of 10 \n")
    if _ace == "0":
        Ace = 1
        print("A is now ", Ace)
    elif _ace == "1":
        Ace = 11
        print("A is now ", Ace)
    else:
        print("Incorrect input, Ace value will be defaulted to 1")

    decktype = input("Choose a deck type [I]nfinite or [S]tandard: \n")
    if decktype == "I" or decktype == "i":
        infDeckGame()
        # exit()
    elif decktype == "S" or decktype == "s":
        stanDeckGame()
        # exit()
    else:
        print("Incorrect input! Ending simulation!")
        exit()


# POLICY
def _PolicySelected(x):
    # POLICY 1
    if x == 1:
        if sumTotal < 17:
            #print("hit, Policy 1")
            hit()
    # POLICY 2
    elif x == 2:
        if sumTotal < 17 and hard:
            #print("hit, Policy 2")
            hit()
    # POLICY 3
    elif x == 3:
        return
    # POLICY 4
    elif x == 4:
        #print("hit, Policy 4")
        hit()
        hit()
    # POLICY 5
    


# Change settings prompt
# settings = input(
#     "Do you want to change settings[Y]? Default: Ace=1, No card replacement \n")
# if settings == "Y" or settings == "y":
#     startGame()


# CHECK IF 21 OR OVER
def check():
    global totalWin
    #print(len(deck))
    if sumTotal == 21:
        #print("21! You win")
        totalWin += 1
        return
    elif sumTotal > 21:
        #print("Bust! You went over 21")
        return

# HIT


def hit():
    if (len(deck)) <= 0:
        return

    global sumTotal
    pick = random.randint(0, len(deck)-1)
    card = deck[pick]
    printLog("card drawn: " + str(card))
    # HARD IF ACE IS NOT IN HAND, SOFT IF ACE IS IN HAND
    if card == Ace or card == Ace:
        hard = False
        #print("Drew an ace: ", Ace)
    else:
        hard = True
        # print("hard \n")

    if standard:
        del deck[pick]
        #print("hit:", len(deck))
    sumTotal += card
    #print("After Hit:", sumTotal, " Deck:", len(deck))
    printLog("New sum after draw: " + str(sumTotal))
    check()
    #_PolicySelected(policy)

# DEAL CARDS


def deal():

    global sumTotal
    global deck
    global totalWin
    #global index1,index2,index3,index4
    #print(len(deck))
    # Random  index for player
    pick1 = random.randint(0, len(deck)-1)
    pick2 = random.randint(0, len(deck)-1)


    # Checks if the same card index is chosen again. Avoids selecting the same card
    while pick2 == pick1:
        pick2 = random.randint(0, len(deck)-1)

    # Select card based on index for player
    
    card1 = deck[pick1]
    card2 = deck[pick2]
    #print(card1,card2)
    #print(card1, card2, len(deck))
    if standard:
        #print(pick1, pick2, card1, card2)
        deck[pick1] = 0
        deck[pick2] = 0
        deck = [i for i in deck if i != 0]
        #print(len(deck),x)
    # REMOVE CARD FROM DECK ONE BY ONE, OTHERWISE SAME CARD CAN BE PICKED

    pick3 = random.randint(0, len(deck)-1)
    pick4 = random.randint(0, len(deck)-1)
    while pick4 == pick3:
        pick4 = random.randint(0, len(deck)-1)
    card3 = deck[pick3]
    card4 = deck[pick4]
    
    printLog("card1-> "+str(card1)+ " card2-> "+ str(card2)+ " card3-> "+str(card3)+" card4-> "+str(card4))
    # REMOVE CARDS FROM DECK
    if standard:
        #print(pick3, pick4, card3, card4)
        deck[pick3] = 0
        deck[pick4] = 0
        deck = [i for i in deck if i != 0]
        #print(len(deck))

    # HARD IF ACE IS NOT IN HAND, SOFT IF ACE IS IN HAND
    if card1 == Ace or card2 == Ace:
        hard = False
        #print("Drew an ace: ", Ace)
    else:
        hard = True
        # print("hard \n")

    # print("Player 1")
    # print("Card 1:", card1)
    # print("Card 2:", card2)
    # print("your sum is: ", card1+card2)

    # print("Player 2")
    # print("Card 3:", card3)
    # print("Card 4:", card4)
    # print("your sum is: ", card3+card4)

    #print("P1 chooses \n")
    sumTotal = card1+card2
    check()  # CHECK WIN/BUST BEFORE HITTING
    _PolicySelected(policy)

    if(policy > 0):
        #print("entering dealer")
        global p1Value
        p1Value = sumTotal # sum plus the hit of p1
        sumTotal = card3+card4
        if card3 == Ace or card4 == Ace:
            printLog("dealer has an ace")
            sumTotal += 10
        check()
        if sumTotal < 21:
            printLog("dealer hit")
            hit()
        if p1Value < 21 and sumTotal < 21:
            #print(x,p1Value, sumTotal, len(deck))
            printLog("p1 and dealer both have less than 21")
            if p1Value > sumTotal:
                printLog("p1 beats dealer "+ str(p1Value)+ " > " + str(sumTotal))
                totalWin+=1
        if p1Value < 21 and sumTotal > 21:
            printLog("dealer busted after drawing and player hasn't busted. So p1 wins")
            totalWin += 1
    


def printLog(mString):
    #display cards
    #print(mString)
    return

# rounds = int(input("Enter a number of rounds \n"))
# policy = int(input("Select a policy to play. 1,2,3,4,5"))
rounds = 1000

policy = 3
#print(policy)

#rounds = 5
#policy = 3
# index1 = 6 #7,6
# index2 = 5 #19
# index3 = 0
# index4 = 1


plotArray = []
_policy3Ar = []
_policy4Ar = []
# _policy3Bar = []
# _policy4Bar = []


def simulate():
    global rounds
    global deck
    global totalWin
    x = 1
    for i in range(15):
        while x <= rounds:
            printLog("Standard Deck? " + str(standard))
            printLog("round start: " + str(x))
            printLog("policy played: " +  str(policy))
            # Create deck and shuffle deck after settings
            deck = [Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]*4
            random.shuffle(deck)
            #print("\n---------------------------------------")
            #print("Round: ", x)
            deal()
            #print("\n")
            printLog("total wins so far: "+ str(totalWin))
            x += 1
            
            #time.sleep(.2)
        x=1
        plotArray.append(totalWin)
        totalWin = 0

simulate()
_policy3Ar = plotArray
policy = 4
plotArray = []
simulate()
_policy4Ar = plotArray

# def runSimulation():
#     global policy, _policy3Ar, _policy4Ar, plotArray
#     simulate()
#     _policy3Ar = plotArray
#     policy = 4
#     plotArray = []
#     simulate()
#     _policy4Ar = plotArray
#     if policy == 4: policy=3

# for i in range(1):
#     runSimulation()
#     print("next rounds")
#     rounds *= 10
#     print("policy bar update:",_policy3Ar)
#     _policy3Bar.append(_policy3Ar)
#     _policy4Bar.append(_policy4Ar)


policy3Avg = st.mean(_policy3Ar)/rounds
policy4Avg = st.mean(_policy4Ar)/rounds
print(_policy3Ar,policy3Avg, _policy4Ar,policy4Avg)
#print("policy bar:", _policy3Bar)
# #xpoints = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# plt.ylim(0,rounds)
# ypoints = np.array(plotArray)

# plt.plot(ypoints)
# plt.show()

plt.ylim(0,1)
barList = plt.bar(["policy 3","policy 4"],[policy3Avg,policy4Avg],)
barList[0].set_color('r')
barList[1].set_color('b')
plt.text(0,1,policy3Avg, ha='center')
plt.text(1,1,policy4Avg, ha='center')
plt.ylabel("Average win rate")
plt.xlabel(str(rounds) + " rounds with 15 iteration")

plt.show()