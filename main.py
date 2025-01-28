import random

cards = ["Face", 2, 3, 4, 5, 6, 7, 8, 9, 10]

def main_menu():
    while True:
        prompt = int(input("""Welcome to Blackjack Elite, presented to you by MiniGame Enterprizes!

In blackjack, each player aims to beat the other by having a hand value closest to 21 without exceeding it.
Here are the rules:
    - Players are dealt two cards and can choose to "hit" (take additional cards) or "stand" (keep their current hand) to achieve the best total. 
    - Face cards are worth 11 points if the players total points are less than 11 total points, and worth 1 point if the total points are 11+ points.
    - To win after the first player plays, the second player should have more points than the first player, but less than 21

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

def rematch(current_game_mode):
    while True:
        rematch = input("Would you like to have a rematch? Type 'y' for yes, or 'n' for no... ")
        if rematch.title() == "Y":
            current_game_mode()
        else:
            print("")
            print("Returning to main menu...")
            print("")
            main_menu()

def cpu_plays(player_count, current_game_mode):
    cpu_count = 0
    while True:
        see_cpus_cards = input("Press enter to see the computers cards: ")
        if len(see_cpus_cards) >= 0:
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
            print("")
            print("The computer's total so far is: ", cpu_count)
            continue
        elif cpu_count > 21:
            print("The computer went past 21, and YOU WIN!!")
            break
    rematch(current_game_mode)

def player_vs_player():
    p1_count = 0
    p2_count = 0
    pass
    

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
        print("")
        print("Your total so far is:", player_count)
        if player_count == 21:
            print("")
            print("You win!! You scored a perfect 21!!")
            rematch(current_game_mode)

        elif player_count < 21:
            print("")
            next_choice = input("""Type "Hit" if you want to continue your turn or "Stand" to pass: """)
            if next_choice.title() == "Hit":
                hit(player_count, current_game_mode)
            elif next_choice.title() == "Stand" and current_game_mode == player_vs_cpu:
                cpu_plays(player_count, current_game_mode)
            elif next_choice.title() == "Stand" and current_game_mode == player_vs_player:
                player_vs_player()
        else:
            print("")
            print("You went over 21. You lost!")
            rematch(current_game_mode)

def player_vs_cpu():
    player_count = 0
    draw_two_cards(player_count, player_vs_cpu)

def draw_two_cards(player_count, current_game_mode):
    
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
                print("")
                next_choice = input("""Type "Hit" if you want to continue your turn or "Stand" to pass: """)
                if next_choice.title() == "Hit":
                    hit(player_count, current_game_mode)
                elif next_choice.title() == "Stand" and current_game_mode == player_vs_cpu:
                    cpu_plays(player_count, current_game_mode)   
                elif next_choice.title() == "Stand" and current_game_mode == player_vs_player:
                    player_vs_player()      

main_menu()