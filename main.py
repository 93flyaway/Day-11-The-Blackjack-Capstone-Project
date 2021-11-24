from replit import clear
from art import logo
import random

def deal_card(hand):
    """returns the parameter list with a randomly chosen card appended to it"""
    return hand.append(random.choice(cards))

def add_aces(hand):
    """returns the total score of an input hand"""
    if 11 not in hand:
        return sum(hand)
    else:
        total = 0
        ace_counted_as_eleven = 0
        # what about [11, 11, 10]
        # if sum of all other numbers are greater than 10, all aces has value of 1.
        # if there are more than 1 aces, a maximum of 1 ace can have the value of 11, since 11 > 10.
        # if the total score is greater than 21 if an ace has a value of 11, ace value should be changed to 1.
        for number in hand:
            if number != 11:
                total += number
        for number in hand:
            if number == 11:
                if total <= 10:
                    total += 11
                    ace_counted_as_eleven += 1
                else: # total > 10
                    total += 1
        if ace_counted_as_eleven > 0 and total > 21:
            total -= 10
        return total


def print_hand(is_gameover_var):
    """prints the hands and scores of both player and computer in a different format, depending on whether the game is over."""
    if is_gameover_var:
        print(f"    Your final hand: {player_hand}, final score: {add_aces(player_hand)}")
        print(f"    Computer's final hand: {computer_hand}, final score: {add_aces(computer_hand)}")  
    else:
        print(f"    Your cards: {player_hand}, current score: {add_aces(player_hand)}")
        print(f"    Computer's first card: {computer_hand[0]}")

def check_21(hand):
    """returns True if a given hand has a score of 21. returns false otherwise."""
    if add_aces(hand) == 21:
        return True
    else:
        return False

def check_bust(hand):
    """returns True if a given hand is bust. returns false otherwise."""
    if add_aces(hand) > 21:
        return True
    else:
        return False
    
def check_blackjack(hand):
    """returns True if given hand is blackjack. returns false otherwise."""
    if sum(hand) == 21 and len(hand) == 2:
        return True
    else:
        return False

def game_result(player_score, computer_score, is_player_bust, is_computer_bust):
    """prints game results"""
    if is_player_bust:
        print("You went over. You lose.")
    elif is_computer_bust:
        print("Opponent went over. You win.")
    elif player_score > computer_score:
        print("You win.")
    elif player_score < computer_score:
        print("You lose.")
    else:
        print("Draw.")

def hit_me():
    """asks user if they want to take another card, as long as they can. if user is bust or user decides to stand, computer is dealt cards and the results are calculated."""
    is_gameover = False
    is_player_bust = False
    is_player_21 = False
    is_computer_bust = False
    # if player hits, if player is no longer able to hit (ie 21 or bust, then deal cards to dealer)
    hit_or_stand = input("Type 'y' to get another card, type 'n' to pass: ")
    #if player wants to hit
    if hit_or_stand == 'y':
        deal_card(player_hand)
        is_player_21 = check_21(player_hand)
        is_player_bust = check_bust(player_hand)
        #if player is no longer able to hit (i.e. 21 or bust)
        if is_player_bust or is_player_21:
            is_gameover = True
            #deal cards to computer until 17 or higher
            while add_aces(computer_hand) < 17:
                deal_card(computer_hand)
            is_computer_bust = check_bust(computer_hand)
            print_hand(is_gameover)
            game_result(add_aces(player_hand), add_aces(computer_hand), is_player_bust, is_computer_bust)
        #if player is still able to hit    
        else:
            print_hand(is_gameover)
            hit_me()
        
    #if player stands
    else:
        #deal cards to computer until 17 or higher
        while add_aces(computer_hand) < 17:
                deal_card(computer_hand)
        #check if computer is bust and print game results
        is_computer_bust = check_bust(computer_hand)
        is_gameover = True
        print_hand(is_gameover)
        game_result(add_aces(player_hand), add_aces(computer_hand), is_player_bust, is_computer_bust)
"""
Functions
**********************************************************************************************************************************************************************
Code
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    print(logo)

    #declare variables
    player_hand = []
    computer_hand = []

    #deal hands
    for round in range(2):
        deal_card(player_hand)
        deal_card(computer_hand)

    is_player_blackjack = check_blackjack(player_hand)
    is_computer_blackjack = check_blackjack(computer_hand)
    is_blackjack = is_player_blackjack or is_computer_blackjack

    #print initial hand and computer's first card
    print_hand(is_blackjack)

    if is_blackjack:
        game_result(sum(player_hand), sum(computer_hand), False, False)
    else:
    #player chooses if he wants to hit or stand until game is over.
        hit_me()


############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

