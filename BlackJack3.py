# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from random import randint

# Define functions

card_rank = randint(1, 13)

def name_of_card(card_name):
    if card_rank == 1:
        card_name = "Ace"
    elif card_rank == 11:
        card_name = "Jack"
    elif card_rank == 12:
    # A 12 stands for a queen.
        card_name = "Queen"
    elif card_rank == 13:
    # A 13 stands for a king.
        card_name = "King"
    else:
    # All other cards are named by their number, or rank.
        card_name = str(card_rank)

    if card_rank == 1 or card_rank == 8:
        print('Drew an ' + card_name)
    else:
        print('Drew a ' + card_name)
    
    return card_name
    

def value_of_card(card_value):
    if card_rank == 11 or card_rank == 12 or card_rank == 13:
    # Jacks, Queens, and Kings are worth 10.
        card_value = 10
    elif card_rank == 1:
    # Aces are worth 11.
        card_value = 11
    else:
    # All other cards are worth the same as their rank.
        card_value = card_rank
    
    return card_value
    

    
#Draw 1st Card.

card_rank_of_first = name_of_card(card1_name)
print(card_rank_of_first)
card_value_of_first = value_of_card(card1_value)
print(card_value_of_first)

# Draw 2nd card.

card_rank_of_second = name_of_card(card2_name)
print(card_rank_of_second)
card_value_of_second = value_of_card(card2_value)
print(card_value_of_second)

#Hand Value

hand_value = card_value_of_first + card_value_of_second


# The user has the option to keep drawing if their hand is below 21.

is_yes = True
while hand_value < 21 and is_yes:
  should_hit = input('You have ' + str(hand_value) + ". Hit (y/n)? ")
  if should_hit == 'n':
    is_yes = False
  elif should_hit == 'y':
    card_name_of_third = name_of_card(card3_name)
    card_value_of_third = value_of_card(card3_value)
    hand_value = hand_value + card_value_of_third
  else:
    print("Sorry I didn't get that.")

print("Final hand: " + str(hand_value) + ".")
if hand_value == 21:
    print("BLACKJACK!")
elif hand_value > 21:
    print("BUST.")