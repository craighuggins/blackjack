#Author: Craig Huggins
#Title: Blackjack game
#Version: 1.0

import random

deck = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11
    }


def get_card_player():
    
    #Create list of cards and values
    player_card_name_list = list(deck.items())
    
    player_selected_card = random.choice(player_card_name_list)
    print(player_selected_card)
    
    player_selected_card_name = player_selected_card[0]
    player_selected_card_value = player_selected_card[1]
    
    #Handle case of an Ace card being dealt
    if player_selected_card_name == "Ace":
        while True:
            try:
                player_ace_choice = int(input("You have been dealt an 'Ace' card. Do you want to choose 1 or 11?: "))
                if player_ace_choice in (1,11):
                    player_selected_card_value = player_ace_choice
                    break
                else:
                    print("You can only choose either 1 or 11 for your Ace value")
            except ValueError:
                print("Provide an integer value, either 1 or 11...")
                continue
    
    return [player_selected_card_name, player_selected_card_value]



def get_card_dealer():
    
    #Create list of cards and values
    dealer_card_name_list = list(deck.items())
    
    dealer_selected_card = random.choice(dealer_card_name_list)
    print(dealer_selected_card)
    
    dealer_selected_card_name = dealer_selected_card[0]
    dealer_selected_card_value = dealer_selected_card[1]
        
    return [dealer_selected_card_name, dealer_selected_card_value]



def player_game():
    
    print('***************** The Players Round *****************')
    
    player_initial_card_1 = get_card_player()
    player_initial_card_2 = get_card_player()
    player_hand = player_initial_card_1[1] + player_initial_card_2[1]

    print('Your initial hand: ', player_hand)
    
    if player_hand == 21:
        print("Automatic WIN!")
        return
    
    
    while True:
        user_action = str(input("Hit or Stay?: "))
        if user_action in ('hit', 'Hit', 'HIT', 'h', 'H'):
            new_card_player = get_card_player()
            player_hand += new_card_player[1]
            print(player_hand)
            if player_hand > 21:
                print("Bust!")
                break
        elif user_action in ('stay', 'Stay', 'STAY', 's', 'S'):
            print('Your final score: ', player_hand)
            break
        else:
            print("You didn't pick an available action. Try again")
            
    print('\n')
            
    return player_hand


def dealer_game():
    
    print('***************** The Dealers Round *****************')
    
    dealer_initial_card_1 = get_card_dealer()
    dealer_initial_card_2 = get_card_dealer()
    dealer_hand = dealer_initial_card_1[1] + dealer_initial_card_2[1]
    
    print('Dealers hand: ', dealer_hand)
    
    while dealer_hand <= 16:
        new_card_dealer = get_card_dealer()
        if new_card_dealer[0] == "Ace":
            if ((dealer_hand + 11) > 21):
                new_card_dealer[1] = 1
            else:
                new_card_dealer[1] = 11
        dealer_hand += new_card_dealer[1]
        print("Dealers Hand", dealer_hand)
        if dealer_hand > 21:
            print("Dealer busts!")
            break
        
    print('\n')
        
    return dealer_hand


def main():
    player = player_game()
    dealer = dealer_game()
    print("Players Hand: ", player)
    print("Dealers Hand: ", dealer)
    
    if ((player <= 21) and (dealer <= 21)):
        if player > dealer:
            print("The player wins!")
        elif player < dealer:
            print("The dealer has won")
        else:
            print("Its a draw")
            
    elif ((player <= 21) and (dealer > 21)):
        print("The player wins!")
        
    elif ((dealer <= 21) and (player > 21)):
        print("The dealer has won")
        
    else:
        print("Its a draw")
        

main()