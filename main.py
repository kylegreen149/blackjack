import random

cards = ["Face", 2, 3, 4, 5, 6, 7, 8, 9, 10]

def main_menu():
    while True:
        prompt = int(input("""Welcome to Blackjack Elite, presented to you by MiniGame Enterprizes!
Blackjack is pretty easy to play. The goal: Try to get to 21, or as close as you can possibly get without going over it.
Here are the rules:
- The game starts with the first player drawing two cards. Based on the card's value, you can
    - "Hit": Saying "Hit" means that you want to draw another card to try to get closer to 21
    - "Stand": Saying "Stand" means that you are satisfyed with where you are, and you feel you have got close to 21 as best as you could.
The catch: Once you say "Stand", your turn is over. It is then the next players turn, if they get closer to 21 than you do, then you lose.
However, if you get above 21, or the player after you goes above 21, then that player loses.
    - If you draw a face card before your total count is 11, the face card's value is equal to 11. 
      If your total is already 11 or higher, the face card's value only equals 1.
Choose a number that corresponds with your game mode choice:
    1) Play Blackjack vs Computer
    2) Play Blackjack vs Player (Pass 'n Play)
    3) Exit Program
Enter choice here: """))
        if prompt == 1:
            current_game_mode = player_vs_cpu
            player_vs_cpu()
        elif prompt == 2:
            current_game_mode = player_vs_player
            player_vs_player()
        elif prompt == 3:
            print("Closing Blackjack. Come back soon...")
            exit()
        else:
            print("")
            print("Only enter a number from 1-3")
            print("")

def cpu_plays(player_count, current_game_mode):
    cpu_count = 0
    while True:
        cpus_two_cards = input("Press enter to see the computers first two cards: ")
        if len(cpus_two_cards) >= 0:
            random_index = random.randint(0, len(cards) - 1) # Draws first card
            random_index2 = random.randint(0, len(cards) - 1) # Draws second card
            random_card = cards[random_index] # Returns first card
            random_card2 = cards[random_index2] # Returns second card

            if random_card == "Face" and cpu_count < 11:
                random_card = 11
            elif random_card2 == "Face" and cpu_count < 11:
                random_card2 = 11
            elif random_card2 == "Face" and cpu_count >= 11:
                random_card2 = 1

        print("The computer drew the following cards:", random_card, random_card2)
        cpu_count = random_card + random_card2
        print("The computer's total so far is:", cpu_count)
        break
    while True:
        if cpu_count > player_count and cpu_count <= 21:
            print("The COMPUTER wins!!")
            break
        elif cpu_count <= player_count and cpu_count <= 21:
            random_index = random.randint(0, len(cards) - 1)
            random_card = cards[random_index]
            if random_card == "Face" and cpu_count < 11:
                random_card = 11
            elif random_card == "Face" and cpu_count > 11:
                random_card = 1
            print("The computer drew:", random_card)
            cpu_count += random_card
            print("The computer's total so far is: ", cpu_count)
            continue
        elif cpu_count > 21:
            print("The computer went past 21, and YOU WIN!!")
            break
    while True:
        rematach = input("Would you like to have a rematch? Type 'y' for yes, or 'n' for no... ")
        if rematach.title() == "Y":
            current_game_mode()
        else:
            print("")
            print("Returning to main menu...")
            print("")
            main_menu()
    

def hit(player_count, current_game_mode):
    while True:
        random_index = random.randint(0, len(cards) - 1)
        random_card = cards[random_index]
        print("You drew the following card:", random_card)
        if random_card == "Face" and player_count < 11:
            random_card = 11
        elif random_card == "Face" and player_count >= 11:
            random_card = 1
        player_count += random_card
        print("Your total so far is:", player_count)
        if player_count == 21:
            print("You win!! You scored a perfect 21!!")
            while True:
                rematach = input("Would you like to have a rematch? Type 'y' for yes, or 'n' for no... ")
                if rematach.title() == "Y":
                    current_game_mode()
                else:
                    print("")
                    print("Returning to main menu...")
                    print("")
                    main_menu()

        elif player_count < 21:
            next_choice = input("""Type "Hit" if you want to continue your turn or "Stand" to pass: """)
            if next_choice.title() == "Hit":
                hit(player_count, current_game_mode)
                break
            elif next_choice.title() == "Stand":
                cpu_plays(player_count, current_game_mode)
        else:
            print("You went over 21. You lost!")
            while True:
                rematach = input("Would you like to have a rematch? Type 'y' for yes, or 'n' for no... ")
                if rematach.title() == "Y":
                    current_game_mode()
                else:
                    print("")
                    print("Returning to main menu...")
                    print("")
                    main_menu()

def player_vs_cpu():
    player_count = 0

    while True:
        users_two_cards = input("Press enter to draw your first two cards: ")
        if len(users_two_cards) >= 0:
            random_index = random.randint(0, len(cards) - 1) # Draws first card
            random_index2 = random.randint(0, len(cards) - 1) # Draws second card
            random_card = cards[random_index] # Returns first card
            random_card2 = cards[random_index2] # Returns second card
            if random_card == "Face" and player_count < 11:
                random_card = 11
            elif random_card2 == "Face" and player_count < 11:
                random_card2 = 11
            elif random_card2 == "Face" and player_count > 11:
                random_card2 = 1

            print("You drew the following cards:", random_card, random_card2)
            player_count = random_card + random_card2
            print("Your total so far is:", player_count)
            if player_count < 21:
                next_choice = input("""Type "Hit" if you want to continue your turn or "Stand" to pass: """)
                if next_choice.title() == "Hit":
                    hit(player_count, player_vs_cpu)
                elif next_choice.title() == "Stand":
                    cpu_plays(player_count, player_vs_cpu)
    # Computer generates card     

def player_vs_player():
    pass
main_menu()