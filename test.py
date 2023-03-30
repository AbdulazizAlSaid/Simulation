import os
import random

deckType = input("Enter type of deck to use [I]nfinite or [S]tandard: ")
policy = int(input("Enter the policy you want to play with 1-5: "))

# user chooses number of decks of cards to use
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

# initialize scores
wins = 0
losses = 0
rounds = 0
def policyChoice(p, player_hand):

    if 'A' in player_hand:
        hard = True
    else:
        hard = False
    # POLICY 1 if hnnd is 17 or above stick, else hit
    if p == 1:
        if total(player_hand)>= 17:
            print("stick, Policy 1")
        elif total(player_hand) < 17:
            print("hit, Policy 1")
            hit(player_hand)
    # POLICY 2 if ace in hand and you are at 17 or above stick, 
    # else if hand is below 17 and ace is in hand and youd ont have 21 then hit
    elif p == 2:
        if total(player_hand) >= 17 and hard:
            print("stick, Policy 2")
        elif total(player_hand) < 17 and hard and total(player_hand)!=21:
            print("hit, Policy 2")
            hit(player_hand)
    # POLICY 3, always stick
    elif p == 3:
        print("stick, Policy 3")
    # POLICY 4, always hit twice
    elif p == 4:
        print("hit, Policy 4")
        hit(player_hand)
        hit(player_hand)
    # POLICY 5: If hand is less than 11 hit twice, else hit once
    elif p == 5:
        if total(player_hand) <=11:
            hit(player_hand)
            hit(player_hand)
        else:
            hit(player_hand)
def deal(deck):
    hand = []
    if deckType == "s" or deckType == "S":
        for i in range(2):
            random.shuffle(deck)
            card = deck.pop()
            if card == 11:card = "J"
            if card == 12:card = "Q"
            if card == 13:card = "K"
            if card == 14:card = "A"
            hand.append(card)
        return hand
    elif deckType == "i" or deckType == "I":
        for i in range(2):
            random.shuffle(deck)
            card =  random.randint(0, len(deck)-1)
            if card == 11:card = "J"
            if card == 12:card = "Q"
            if card == 13:card = "K"
            if card == 14:card = "A"
            hand.append(card)
        return hand
     
def play_again():
    """
    again = input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
    """
    dealer_hand = []
    player_hand = []
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
    
    """
    else:
        print("Bye!")
        exit()
    """
def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total+= 10
        elif card == "A":
            if total >= 11: total+= 1
            else: total+= 11
        else: total += card
    return total

def hit(hand):
     if deckType == "s" or deckType == "S":
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
        return hand
     elif deckType == "i" or deckType == "I":
        card = random.randint(0, len(deck)-1)
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
        return hand
def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def print_results(dealer_hand, player_hand):
    clear()

    print("\n    WELCOME TO BLACKJACK!\n")
    print("-"*30+"\n")
    print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))
    print("-"*30+"\n")
    print ("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
    print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand):
    global wins
    global losses
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Congratulations! You got a Blackjack!\n")
        wins += 1
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Sorry, you lose. The dealer got a blackjack.\n")
        losses += 1
        play_again()

def score(dealer_hand, player_hand):
        # score function now updates to global win/loss variables
        global wins
        global losses
        if total(player_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("Congratulations! You got a Blackjack!\n")
            wins += 1
        elif total(dealer_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("Sorry, you lose. The dealer got a blackjack.\n")
            losses += 1
        elif total(player_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("Sorry. You busted. You lose.\n")
            losses += 1
        elif total(dealer_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("Dealer busts. You win!\n")
            wins += 1
        elif total(player_hand) < total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
            losses += 1
        elif total(player_hand) > total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Congratulations. Your score is higher than the dealer. You win\n")
            wins += 1

def game():
    global wins
    global losses
    choice = 0
    rounds = 0
    policy = 0
    clear()
    print("\n    WELCOME TO BLACKJACK!\n")
    rounds = int(input("Choose how many rounds to play: \n"))
    print("-"*30+"\n")
    print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))
    print("-"*30+"\n")
    dealer_hand = deal(deck)
    player_hand = deal(deck)

    #print ("The dealer is showing a " + str(dealer_hand[0]))
    #print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
    #blackjack(dealer_hand, player_hand)
    #quit=False
    i = 1
    while i<=rounds:
    
        print("-"*30+"\n")
        print("    \033[1;32;40mWINS:  \033[1;37;40m%s   \033[1;31;40mLOSSES:  \033[1;37;40m%s\n" % (wins, losses))
        print("-"*30+"\n")
        dealer_hand = deal(deck)
        player_hand = deal(deck)
        print ("The dealer is showing a " + str(dealer_hand[0]))
        print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
        blackjack(dealer_hand, player_hand)
        """
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        if choice == 'h':
            hit(player_hand)
            print(player_hand)
            print("Hand total: " + str(total(player_hand)))
        """
        policyChoice(policy, player_hand)
        if total(player_hand)>21:
            print('You busted')
            losses += 1
            play_again()

        #elif choice=='s':
        while total(dealer_hand)<17:
            hit(dealer_hand)
            print(dealer_hand)
            if total(dealer_hand)>21:
                print('Dealer busts, you win!')
                wins += 1
                play_again()
        score(dealer_hand,player_hand)
        play_again()
        i+=1


if __name__ == "__main__":
   game()
