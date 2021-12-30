"""
Rules:

Deal out 4 cards to each player. 
Deal one card face up on the game board.

Each player can view 2 of the 4 cards they received
    - We'll just let them view all 4
    - The computer will pick these randomly for both
    the computer and the player

Scores:

    Kings = 0
    Ace = 1
    2 = 2
    3 = 3
    etc...
    10's/Jacks/Queens = 10

Players can draw from the card that is face up on the board
or from the deck.
    - They can keep this card and trade it out for any of
    their 4 cards or they can make it the card that is
    face up on the board

Either player can "knock" to signal they are ready to 
end the game. The player that didn't knock gets one
more draw and then everyone revelas their cards.

The person with the lowest score wins.

"""
from rank import Rank
from suit import Suit
from card import Card
from player import Player

from random import shuffle


def process_choice(current_player, face_up, current_card):
    if current_player == computer:

        if sum([card.value for card in current_player.hand]) < 18:
            return KNOCK

        max_value = max(current_player.hand).value
        if face_up.value < max_value:
            return KEEP_FACE_UP

        if current_card.value < max_value:
            return KEEP_CURRENT

        return DO_NOTHING

    return int(input(f"What do you want to do? {options} "))


deck = []
for rank in Rank:
    for suit in Suit:
        deck.append(Card(rank, suit))


shuffle(deck)

player = Player("Daniel")
computer = Player("Computer")

player.hand = [deck.pop() for _ in range(4)]
computer.hand = [deck.pop() for _ in range(4)]

options = """
    1.) Keep face up
    2.) Keep current
    3.) Do nothing
    4.) Knock
"""

current_player = player

face_up = deck.pop()

KEEP_FACE_UP = 1
KEEP_CURRENT = 2
DO_NOTHING = 3
KNOCK = 4

rounds_left = None


while True:
    current_card = deck.pop()
    print(f"\n{current_player=}")
    print(f"{current_player.hand=}")
    print(f"{face_up=}")
    print(f"{current_card=}")

    choice = process_choice(current_player, face_up, current_card)

    if choice in (KEEP_FACE_UP, KEEP_CURRENT):
        discarded_index = current_player.hand.index(max(current_player.hand))
        discarded = current_player.hand.pop(discarded_index)

    if choice == KEEP_FACE_UP:
        print(f"{current_player.name} discarding {discarded} for {face_up}")
        current_player.hand.append(face_up)
        face_up = current_card
    elif choice == KEEP_CURRENT:
        print(f"{current_player.name} discarding {discarded} for {current_card}")
        current_player.hand.append(current_card)
    elif choice == DO_NOTHING:
        face_up = current_card
    elif choice == KNOCK:
        print(f"{current_player.name} KNOCKS!")
        rounds_left = 1
        

    if current_player == player:
        current_player = computer
    else:
        current_player = player

    if rounds_left is not None:
        if rounds_left:
            rounds_left -= 1
        else:
            break



computer_score = sum([card.value for card in computer.hand])
player_score = sum([card.value for card in player.hand])

print(f"{player_score=}")
print(f"{computer_score=}")

if player_score < computer_score:
    print(f"{player.name} wins!")
elif computer_score < player_score:
    print("Computer wins!")
else:
    print("It's a tie!")