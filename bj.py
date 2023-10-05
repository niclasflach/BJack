"""
Black Jack, assignement Pythonprogrammering för AI
"""
import random
import keyboard
import time
import os

__author__ = "Niclas Flach"
__version__ = "0.1.0"

DECK_COLORS = ["♠","♥","♦","♣"]

class Card :

    def __init__(self, color , valor):
        self.color = color
        self.valor = valor
        if valor > 10 and valor < 14:
            self.value = 10
        elif valor == 14:
            self.value = 11
        else:
            self.value = valor
    def show(self):
        print(f"{self.color}{self.valor} has the value:{str(self.value)}")
            
class Deck():
    
    def __init__(self):
        self.cards = []
        self.build ()


    def build(self):
        for s in DECK_COLORS:
            for v in range (1 , 15) :
                self.cards.append(Card(s , v))

    def shuffle(self):
        random.shuffle(self.cards)

    def visa_kort(self):
        for card in self.cards:
            card.show()
    
class Player :

    def __init__(self):
        self.money = 100
        self.card_in_hand = []
        self.hand_value = 0
    
    def get_cards(self):
        return [card for card in self.card_in_hand]
    def cards_reset(self):
        self.hand_value = 0 
        self.card_in_hand = []
    
    def print_cards(self):
        self.hand_value = 0
        for card in self.card_in_hand:
            print(f"{card.color}{card.valor} värde: {card.value}")
            self.hand_value += card.value
        print (f"kortens värde: {self.hand_value}")

    

def main():
    player = Player()
    dealer = Player()
    """ Main entry point of the app """
    def draw_screen():
        os.system('cls')
        print(f"-----Bet:${bet}----------")
        print(f"Dealers cards: ")
        dealer.print_cards()
        print("-----------------------")
        print(f"You have ${player.money}")
        print(f"Players cards: ")
        player.print_cards()
        print("---------------------------")
        print("| tryck h för att ta kort |")
        print("| tryck s för att stanna  |")
        print("---------------------------")
        return
    def game():
        deck = Deck()
        deck.shuffle()
        dealing = True
        player.card_in_hand.append(deck.cards.pop())
        dealer.card_in_hand.append(deck.cards.pop())
        player.card_in_hand.append(deck.cards.pop())
        while dealing:
            draw_screen()
            if player.hand_value >21:
                player.money -= bet
                draw_screen()
                print("Du blev tjock")
                dealing = False
                break
            while True:
                key = keyboard.read_key()
                if key == 'h':
                    player.card_in_hand.append(deck.cards.pop())
                    print("Tar ett kort...")
                    time.sleep(2)
                    break
                elif key == 's':
                    dealing = False
                    while dealer.hand_value < 17:
                        print("Dealern tar ett kort")
                        time.sleep(2)
                        dealer.card_in_hand.append(deck.cards.pop())
                        draw_screen()
                    if dealer.hand_value > player.hand_value and dealer.hand_value < 22:
                        print("Dealern vann...")
                        player.money -= bet
                        draw_screen()
                        time.sleep(1)
                        break
                    elif dealer.hand_value == player.hand_value:
                        print("Det blev lika")
                        break
                    else:
                        print("Du vann")
                        player.money += bet
                        draw_screen()
                        time.sleep(1)
                        break
        return
    bet = 10
    while True:           
        game()
        print("Spela igen (c för att ändra bet) (j/n)")
        while True:
            key = keyboard.read_key()
            if key == 'j':
                print("Blandar kortleken...")
                player.cards_reset()
                dealer.cards_reset()
                time.sleep(1)
                break
            if key == 'c':
                bet = int(input("Ny bet storlek:"))
                print(f"Nytt bet : ${bet}")
                print("Blandar kortleken...")
                player.cards_reset()
                dealer.cards_reset()
                time.sleep(1)
                break
            elif key == 'n':
                quit()
        
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()