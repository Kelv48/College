from random import shuffle

class Hand:
    def __init__(self):
        self.hand = []
    
    #Takes the popped card and adds it to the deck
    def add_card(self, card):
        self.hand.append(card)

    #Runs a function to get the highest card in the players hand
    def get_highest_card(self):
        if not self.hand:
            return None
        return max(self.hand, key=lambda card: card.card_number)
    
    #Converts it to a str to make it printable easily
    def __str__(self):
        return ', '.join(str(card) for card in self.hand)

class Card:
    #Initialize the card function passing in the suit and card_number info
    def __init__(self, card_number, suit):
        self.card_number = card_number
        self.suit = suit
    
    #A built in python function that turns objects to strings
    #used to turn the card objects into strings
    def __str__(self):
        return f'{self.card_number}{self.suit}'
    
    #Checks the card number and suit to see if both are equal to find out if the cards are the same
    def is_equal(self, other):
        return self.card_number == other.card_number and self.suit == other.suit
    
    #Checks if the card number is higher 
    #Needs a fix for A, J, Q, K add in dictionary translation
    def is_higher(self, other):
        return self.card_number > other.card_number

class Deck:
    def __init__(self):
        self.deck = self.create_deck()
        self.shuffle_deck()
        
    #Creates a deck of 52 playing cards
    def create_deck(self):
        deck = []
        suits = ["♠", "♦", "♥", "♣"]
        # card_numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for num in range(1, 13):
            for suit in suits:
                card = Card(num, suit)
                deck.append(card)
        return deck

    #Takes your deck and shuffles it randomly
    def shuffle_deck(self):
        shuffle(self.deck)
    
    #Deals a card from the deck and pops it from the deck
    def deal_card(self):
        if not self.deck:
            return None
        return self.deck.pop()

def play_game():
    #creates a deck, player hand and computer hand
    deck = Deck()
    player_hand = Hand()
    computer_hand = Hand()

    #Deals 5 cards to both the player and the computer
    for _ in range(5):
        player_card = deck.deal_card()
        computer_card = deck.deal_card()
        player_hand.add_card(player_card)
        computer_hand.add_card(computer_card)

    #Show the player their hand
    print("Your hand: ", player_hand)
    highest_player_card = player_hand.get_highest_card()
    
    #Ask the player for their prediction
    prediction = input("Do you think you have the highest card? (yes/no): ")
    if prediction.lower() == 'yes':
        highest_computer_card = computer_hand.get_highest_card()
        if highest_player_card.is_higher(highest_computer_card):
            print("You have the highest card. You win!")
        else:
            print("You don't have the highest card. You lose.")
    elif prediction.lower() == 'no':
        highest_computer_card = computer_hand.get_highest_card()
        if highest_computer_card.is_higher(highest_player_card):
            print("The computer card is higher. You guessed right.")
        else:
            print("Your card is higher you guessed wrong")
    else:
        print("You chose not to predict.")

#Makes sure the game only runs if the script is run as the main program
if __name__ == "__main__":
    play_game()
