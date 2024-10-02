import random

#Use capital letter for the first letter of the class name, only for humans.
class Deck:
    #the constructor, instantiate
    def __init__(self):
        self.deck = []
        self.generate_deck(self.deck)
        self.shuffle_deck(self.deck)

    def generate_deck(self, cardDeck):
        # cardDeck = []
        # cardNumbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        cardSuits = ["♠", "♦", "♥", "♣"]

        for num in range(1, 13):
            for suit in cardSuits:
                card = str(num) + suit
                cardDeck.append(card)
        return cardDeck

    def shuffle_deck(self, cardDeck):
        random.shuffle(cardDeck)

    def dealCard(self):
        if not self.deck:
            return None
        return self.deck.pop()



class Hand:
    def __init__(self):
        self.hand = []

    def dealCard(self, card):
        self.hand.append(card)

    def highestCard(self):
        if not self.hand:
            return None
        else:
            tempHand = []
            for card in self.hand:
                card = card[:-1]
                if card == "1":
                    card = "14"
                tempHand.append(int(card))      
            return max(tempHand)
        
    def __str__(self):
        return ', '.join(str(card) for card in self.hand)


class Card:
    def __init__(self, cardNumber, cardSuit):
        self.number = cardNumber
        self.suit = cardSuit

    def __str__(self):
        return f"{self.number}{self.suit}"
    
    # def isEqual(self, comparison):
    #     return self.number == comparison.number and self.suit == comparison.suit
    
    def isHigher(card, comparison):
        if card > comparison:
            return True
        elif comparison > card:
            return False
    
    def cleanCards(cardDeck):
        cleanedDeck = []
        for card in cardDeck.hand:
            symbol = card[len(card)-1]
            card = card[: -1]
            if int(card) == 1:
                card = "A" + symbol
            elif int(card) == 11:
                card = "J" + symbol
            elif int(card) == 12:
                card = "Q" + symbol
            elif int(card) == 13: 
                card = "K" + symbol
            else:
                card += symbol
            cleanedDeck.append(card)
        return cleanedDeck

def startGame():
    deck = Deck()
    player1Hand = Hand()
    player2Hand = Hand()
    
    #deals 5 cards to each hand
    for i in range(5):
        #Deals the card
        player1Card= deck.dealCard()
        player2Card = deck.dealCard()
        #Deals the card into the players hand/Insert the card into players hand
        player1Hand.dealCard(player1Card)
        player2Hand.dealCard(player2Card)


    p1HighCard = player1Hand.highestCard()
    p2HighCard = player2Hand.highestCard()

    cleanedP1 = Card.cleanCards(player1Hand)
    print("Your cards: ", cleanedP1)
    cleanedP2 = Card.cleanCards(player2Hand)

    question = input("Do you have the highest card against P2? ")
    answer = question.lower()
    if answer == "yes" :
        if Card.isHigher(p1HighCard, p2HighCard) == True:
            print("This was P2 cards: ", cleanedP2)
            print("You win")
        elif Card.isHigher(p1HighCard, p2HighCard) == False:
            print("This was P2 cards: ", cleanedP2)
            print("P2 has the highest card")
        else:
            print("This was P2 cards: ", cleanedP2)
            print("You have have equal high cards!")
    elif answer == "no":
        if Card.isHigher(p2HighCard, p1HighCard) == True:
            print("This was P2 cards: ", cleanedP2)
            print("You win")
        elif Card.isHigher(p2HighCard, p1HighCard) == False:
            print("This was P2 cards: ", cleanedP2)
            print("You do have the highest card against P2")
        else:
            print("This was P2 cards: ", cleanedP2)
            print("You both have equal high cards!")
    else: 
        print("Please submit a valid answer!")


if __name__ == "__main__":
    startGame()