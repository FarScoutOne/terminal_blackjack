# Terminal blackjack
# by: Ryne Smith
# started on: 8/1/2021

# Greeting
print("Welcome to table 3.")
print("Please, have a seat.")

# Required modules
import random

# Create classes and define global variables
class Player:
    def __init__(self, name):
        self.name = name
        self.cards_in_hand = []
        self.hand_value = 0
        self.total_score = 0

class Deck:
    def __init__(self):
        self.cards = [
        # Hearts
        [2,'H'], [3,'H'], [4,'H'], [5,'H'], [6,'H'], [7,'H'], [8,'H'], [9,'H'], [10,'H'],
        ['J','H'], ['Q','H'], ['K','H'], ['A','H'],
        # Diamonds
        [2,'D'], [3,'D'], [4,'D'], [5,'D'], [6,'D'], [7,'D'], [8,'D'], [9,'D'], [10,'D'],
        ['J','D'], ['Q','D'], ['K','D'], ['A','D'],
        # Clubs
        [2,'C'], [3,'C'], [4,'C'], [5,'C'], [6,'C'], [7,'C'], [8,'C'], [9,'C'], [10,'C'],
        ['J','C'], ['Q','C'], ['K','C'], ['A','C'],
        # Spades
        [2,'S'], [3,'S'], [4,'S'], [5,'S'], [6,'S'], [7,'S'], [8,'S'], [9,'S'], [10,'S'],
        ['J','S'], ['Q','S'], ['K','S'], ['A','S'],
        ]

    # Returns a random card popped out of the remaining cards in the deck
    def remove_card(self):
        top_card = self.cards.pop(random.randint(0, len(self.cards)))

        return top_card
