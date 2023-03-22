import os, random, string, math

A = 1
J=Q=K=10
deck = [A,2,3,4,5,6,7,8,9,10,J,Q,K]*4

def infDeckGame():
    print ("You have chosen an infinite deck!\n")
def stanDeckGame():
    print ("You have chosen a standard deck!\n")

def startGame():
    decktype = 0
    print ("Welcome to Blackjack simulation, where we will test how often we bust based on predetermined policies!\n")
    decktype = input( "Choose a deck type [I]nfinite or [S]tandard: \n")
    if decktype == "I" or decktype == "i":
        infDeckGame()
        exit()
    elif decktype == "S" or decktype == "s":
        stanDeckGame()
        exit()
    else:
        print("Incorrect input! Ending simulation!")
        exit()


startGame()