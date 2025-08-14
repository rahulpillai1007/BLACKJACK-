
#Rahul Pillai
#Blackjack
import random
import time
player_card1 = random.randint(1, 10)
player_card2 = random.randint(1, 10)
player_total = player_card1 + player_card2

print("Your cards:", [player_card1, player_card2])
print("Your total is:", player_total)

# User's Turn
player_cards = [player_card1, player_card2]
player_choice = ''
while player_choice != 'stand' and player_total <= 21:
    player_choice = input("Do you want to hit or stand? (hit/stand): ")

    if player_choice == 'hit':
        new_card = random.randint(1, 10)
        player_total += new_card
        player_cards = player_cards + [new_card]
        print("\nYou draw:", new_card)
        print("Your cards:", player_cards)
        print("Your total is:", player_total)

    elif player_choice != 'stand':
        print("\nInvalid input! Enter 'hit' to hit or 'stand' to stand.")

# Dealer's Turn
if player_total <= 21:
    dealer_card1 = random.randint(1, 10)
    dealer_card2 = random.randint(1, 10)
    dealer_total = dealer_card1 + dealer_card2
    print("\nDealer's cards:", [dealer_card1, dealer_card2])
    print("Dealer's total is:", dealer_total)

    while dealer_total < player_total and dealer_total <= 21:
        new_card = random.randint(1, 10)
        dealer_total += new_card
        time.sleep(2)
        print("Dealer decides to hit!")
        print("\nDealer draws:", new_card)
        print("Dealer's cards:", [dealer_card1, dealer_card2, new_card])
        print("Dealer's total is:", dealer_total)

# Determine the winner
if player_total > 21:
    print("\nYou bust! Dealer wins.")
elif dealer_total > 21:
    print("\nPlayer wins!")
elif dealer_total > player_total:
    print("\nDealer wins!")
else:
    print("\nDealer wins in a tie")
