import random

def main_menu():
    while True:
        prompt = int(input("""Welcome to Blackjack Elite, presented to you by MiniGame Enterprizes!
Blackjack is pretty easy to play. The goal: Try to get to 21, or as close as you can possibly get without going over it.
Here are the rules:
- The game starts with the first player drawing two cards. Based on the card's value, you can
    - "Hit": Saying "Hit" means that you want to draw another card to try to get closer to 21
    - "Stand": Saying "Stand" means that you are satisfyed with where you are, and you feel you have got close to 21 as best as you could.
The catch: Once you stay "Stand" your turn is over. It is then the next players turn, if they get closer to 21 than you do, then you lose.
However, if you get above 21, or the player after you goes above 21, then that player loses.
    - If you draw a face card before your total count is 11, the face card's value is equal to 11. 
      If your total is already 11 or higher, the face card's value only equals 1.
Choose a number that corresponds with your game mode choice:
    1) Play Blackjack vs Computer
    2) Play Blackjack vs Player (Pass 'n Play)
    3) Exit Program
Enter choice here: """))
        if prompt == 1:
            player_vs_cpu()
        elif prompt == 2:
            player_vs_player()
        elif prompt == 3:
            print("Closing Blackjack. Come back soon...")
            exit()
        else:
            print("")
            print("Only enter a number from 1-3")
            print("")

def player_vs_cpu():
    player_count = 0
    computer_count = 0

    while True:
        cards = ["Face", 2, 3, 4, 5, 6, 7, 8, 9, 10]

        users_two_cards = input("Press enter you draw your first two cards")
        if users_two_cards == "":
            random_index = random.randint(0, len(cards) - 1) # Draws first card
            random_index2 = random.randint(0, len(cards) - 1) # Draws second card
            random_card = cards[random_index] # Returns first card
            random_card2 = cards[random_index2] # Returns second card
            print("You drew the following cards:", random_card, random_card2)
            player_count = random_card + random_card2
            print("Your total is: ", player_count)
        break

def player_vs_player():
    pass
main_menu()