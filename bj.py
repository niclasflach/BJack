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
        #Initiering av player
        #pengar att starta med
        self.money = 100
        #tom lista med korten som objectet har på hand
        self.card_in_hand = []
        #sammanräkning av värdet på handen.
        #Måste lösa hur Ess hanteras!
        self.hand_value = 0
    
    
    def cards_reset(self):
        self.hand_value = 0 
        self.card_in_hand = []
    
    def print_cards(self):
        #nollställer handensvärde då jag gör en ny beräkning när korten printas
        self.hand_value = 0 
        for card in self.card_in_hand:#Ittererar genom korten som är på hand
            print(f"{card.color}{card.valor} värde: {card.value}") #Printar kort
            self.hand_value += card.value #Adderar kortets värde till handens
        print (f"kortens värde: {self.hand_value}") #Printar handens värde

    

def main():
    player = Player() #skapar object av klassen player för spelaren
    dealer = Player() #skapar object av klassen player för dealern
    
    
    def draw_screen():
        '''
        Funktion för att rita skärmen
        '''
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
        deck = Deck() #skapar object av klassen Deck dvs kortlek
        deck.shuffle() #anropar method för att blandda kortleken.
        dealing = True # Omgång pågår
        
        #Drar dom obligatoriska korten
        player.card_in_hand.append(deck.cards.pop())
        dealer.card_in_hand.append(deck.cards.pop())
        player.card_in_hand.append(deck.cards.pop())
        
        
        while dealing: #loop för en omgång
            draw_screen()
            if player.hand_value >21:
                player.money -= bet
                draw_screen()
                print("Du blev tjock")
                dealing = False
                break
            #while loop för att få tangentbordsnedtryckning
            #Går säkert att lösa snyggare men duger så länge
            while True:
                key = keyboard.read_key()
                if key == 'h':
                    #Spelaren tar ett kort
                    player.card_in_hand.append(deck.cards.pop())
                    print("Tar ett kort...")
                    time.sleep(2)
                    break
                elif key == 's':
                    #Spelare stannar!
                    dealing = False
                    while dealer.hand_value < 17:
                        #Dealern tar kort så länge det är under 17.
                        print("Dealern tar ett kort")
                        time.sleep(2)
                        dealer.card_in_hand.append(deck.cards.pop())
                        draw_screen()
                    #Dealern har tagit färdigt kort.
                    #Nu tar vi reda på vem som vann
                    if dealer.hand_value > player.hand_value and dealer.hand_value < 22:
                        #dealern är inte tjock och har högre värde än spelaren
                        print("Dealern vann...")
                        player.money -= bet# Så då tar vi pengar från spelaren
                        draw_screen() #och ritar om skärmen
                        time.sleep(1) #och väntar en sekund för dramatikens skull =)
                        break
                    elif dealer.hand_value == player.hand_value:
                        #Dealer och spelare har samma värde
                        print("Det blev lika")
                        #Inga pengar delas ut eller dras av
                        break
                    else:
                        #Ojdå spelaren vann
                        print("Du vann")
                        player.money += bet #Ger spelaren pengar
                        draw_screen() # Ritar om skärmen
                        time.sleep(1) # och en sekunds paus
                        break
        return
    
    
    bet = 10 # default värde för insatsen
    #Main loopen
    while True:
                   
        game() #starta en om gång
        print("Spela igen (c för att ändra bet) (j/n)") #fråga spelaren om han vill spela en gång till
        
        while True:# Och väntar på tangetbordsnedtryckning
            key = keyboard.read_key()
            if key == 'j':
                # En om gång till på gång!
                print("Blandar kortleken...")
                player.cards_reset()
                dealer.cards_reset()
                time.sleep(1)
                break
            
            if key == 'c':
                #spelaren vill ändra bet
                #lägga detta i funktion?
                bet = int(input("Ny bet storlek:"))
                print(f"Nytt bet : ${bet}")
                print("Blandar kortleken...")
                player.cards_reset()
                dealer.cards_reset()
                time.sleep(1)
                break
            
            elif key == 'n':
                #Spelaren har tröttnat så vi avslutar
                quit()
        
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()