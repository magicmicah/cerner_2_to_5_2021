# cerner_2tothe5th_2021
# Goal is to get to 21. Aces are always worth 11, if I had more time and lines I could possibly do different logic, but alas, its what you are stuck with.
# Best to run this in a console that has unicode support. Windows terminal and any modern bash shell should work, but command prompt will show ugliness Im sure. 
import random, os
playing = True; dealer_score = 0; player_score = 0; 
def reshuffle_deck(): return ["2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", "A♣", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", "A♠", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", "A♥"]
def deal(): choice = random.choice(deck); deck.remove(choice); return choice
def deal_cards(): player_cards.append(deal()); dealer_cards.append(deal())
def calculate_hand_value(hand):
    value = 0
    for i in hand:
        if i[0] in ["K", "Q", "J", "10"]: i = 10
        elif i[0] == "A": i = 11
        else: i = int(i[0])
        value = i + value
    return value
def finish_hand(player_cards, player_score, dealer_cards, dealer_score):
    player_hand = calculate_hand_value(player_cards); dealer_hand = calculate_hand_value(dealer_cards); bigger_value = max(player_hand, dealer_hand)
    if ((player_hand == 21 and dealer_hand == 21) or (player_hand > 21 and dealer_hand > 21) or (player_hand == dealer_hand)): print(f"Dealer hand {dealer_cards} has value of: {dealer_hand}\nPlayer hand {player_cards} has value of: {player_hand}.\nIt's a push. No one wins."); return player_score, dealer_score
    elif (player_hand <= 21 and player_hand == bigger_value): print(f"Dealer hand {dealer_cards} has value of: {dealer_hand}\nPlayer hand {player_cards} has value of: {player_hand}.\nPlayer wins."); player_score = player_score + 1; return player_score, dealer_score
    elif (dealer_hand <= 21 and dealer_hand == bigger_value): print(f"Dealer hand {dealer_cards} has value of: {dealer_hand}\nPlayer hand {player_cards} has value of: {player_hand}.\nDealer wins."); dealer_score = dealer_score + 1; return player_score, dealer_score
    elif(player_hand > 21): print(f"Dealer hand {dealer_cards} has value of: {dealer_hand}\nPlayer hand {player_cards} has value of: {player_hand}.\nDealer wins."); playing = False; dealer_score = dealer_score + 1; return player_score, dealer_score
    elif(dealer_hand > 21): print(f"Dealer hand {dealer_cards} has value of: {dealer_hand}\nPlayer hand {player_cards} has value of: {player_hand}.\nPlayer wins."); playing = False; player_score = player_score + 1; return player_score, dealer_score
while playing is True:
    if(os.name == 'nt'): os.system('cls')
    else: os.system('clear')
    player_cards = []; dealer_cards = [];deck = reshuffle_deck(); deal_cards(); deal_cards()
    player_hand = calculate_hand_value(player_cards); dealer_hand = calculate_hand_value(dealer_cards);
    print(f"Dealer score: {dealer_score}\nPlayer score: {player_score}\n"); print(f"Dealer has {dealer_cards[0]}.\nPlayer has {player_cards} with value of {player_hand}"); hit_or_stay = input("Hit or stay?\n")
    if (hit_or_stay == "hit"):
        player_cards.append(deal()); 
    if (dealer_hand <= 17): dealer_cards.append(deal())
    player_score, dealer_score = finish_hand(player_cards, player_score, dealer_cards, dealer_score)
    play_again = input("Press enter to deal again, anything else to quit\n")
    if (play_again != ""): playing = False