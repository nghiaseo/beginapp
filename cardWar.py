import msvcrt
import os

suits = ['♥', '♦', '♣', '♠']
values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

class Card:
    def __init__(self, suit, value):
        self.suit = suit        
        self.value = value

    def getRank(self):        
        return values.index(self.value)
    

class Deck:
    def __init__(self,cards = []):
        self.deck = cards      
        
                
    def display(self):
        for card in self.deck:
            print(card.value + ' of ' + card.suit)
            
    def shuffle(self):
        import random
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    def draw(self, deck):        
        self.hand.insert(0,deck.deal())
        return self
        
    def display(self,hide = False):
        if hide:
            print(self.name,'('+str(len(self.hand))+')','\n', 'Bottom :',", ".join(['*-*' for card in self.hand]),' : Top')
        else:
            print(self.name,'('+str(len(self.hand))+')','\n','Bottom :', ", ".join([card.value + '-' + card.suit for card in self.hand]),' : Top')

            
    def play(self):
        return self.hand.pop()
    
    def is_empty(self):
        return len(self.hand) == 0
    
def Game():    
    os.system('cls')
    cards = []
    player1 = Player('You')
    player2 = Player('Computer')

    # Create a deck of cards
    for suit in suits:
        for value in values:
            cards.append(Card(suit,value))
    deck = Deck(cards)
    deck.shuffle()
    # distribute the cards
    
    while len(deck.deck) > 0:
        player1.draw(deck)
        player2.draw(deck)

    #begin the game
    #show the cards
    player1.display()
    player2.display(True)

    while not player1.is_empty() and not player2.is_empty():
        print('ESC to exit or Press any key to play the next card...')
        key =  msvcrt.getch()
        if ord(key) == 27:
            break
        card1 = player1.play()
        card2 = player2.play()
        print(player1.name,':',card1.value + '-' + card1.suit)
        print(player2.name,':',card2.value + '-' + card2.suit)
        if card1.getRank() > card2.getRank():
            print(player1.name,'wins')
            msvcrt.getch()
            os.system('cls')
            player1.draw(Deck([card1]))
            player1.draw(Deck([card2]))
        elif card1.getRank() < card2.getRank():
            print(player2.name,'wins')
            msvcrt.getch()
            os.system('cls')
            player2.draw(Deck([card1]))
            player2.draw(Deck([card2]))
        else:
            print('War!')
            war(player1,player2,[card1,card2])

            # player1.draw(deck)
            # player2.draw(deck)
        
        #show the cards
        player1.display()
        player2.display(True)    

def war(player1,player2,pool = []):
    if len(player1.hand) < 2:
        print(player1.name,'does not have enough cards to play war')
        print(player2.name,'wins')
        msvcrt.getch()        
        os.system('cls')
    elif len(player2.hand) < 2:
        print(player2.name,'does not have enough cards to play war')
        print(player1.name,'wins')
        msvcrt.getch()
        os.system('cls')        
    else:
        war_card1_1 = player1.play()
        war_card1_2 = player1.play()
        war_card2_1 = player2.play()
        war_card2_2 = player2.play()
        print(player1.name,':','*-*',war_card1_2.value + '-' + war_card1_2.suit)
        print(player2.name,':','*-*',war_card2_2.value + '-' + war_card2_2.suit)
        if war_card1_2.getRank() > war_card2_2.getRank():
            print(player1.name,'wins')
            msvcrt.getch()
            os.system('cls')
            for card in pool+[war_card1_1,war_card1_2,war_card2_1,war_card2_2]:
                player1.draw(Deck([card]))            
        elif war_card1_2.getRank() < war_card2_2.getRank():
            print(player2.name,'wins')            
            msvcrt.getch()
            os.system('cls')
            for card in pool+[war_card1_1,war_card1_2,war_card2_1,war_card2_2]:
                player2.draw(Deck([card]))            
        else:
            print('War again!')
            msvcrt.getch()
            war(player1,player2,pool + [war_card1_1,war_card1_2,war_card2_1,war_card2_2])
            msvcrt.getch()
        
