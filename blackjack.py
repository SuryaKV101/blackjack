import random
from p1_random import P1Random

rng = P1Random()

# declare variables
game_continue = True
player_wins, dealer_wins, tie_games, game_num = 0, 0, 0, 0

# main while condition, to terminate for choice 4
while game_continue:
    # 1. set up initial message
    card = rng.next_int(13) + 1
    # declare other rest of the variables
    dealer_hand = 0
    player_hand = 0
    game_num += 1
    print("START GAME #", game_num)

    # 2. deal a card to the player
    if card == 1:
        print("\nYour card is a ACE!")
        player_hand += card
    elif 2 <= card <= 10:
        print(f"\nYour card is a {card}!")
        player_hand += card
    elif card == 11:
        print("\nYour card is a JACK!")
        card = 10
        player_hand += card
    elif card == 12:
        print("\nYour card is a QUEEN!")
        card = 10
        player_hand += card
    elif card == 13:
        print("\nYour card is a KING!")
        card = 10
        player_hand += card

    # print hard value information
    print("Your hand is:", player_hand, "\n")

    # 3. keep asking user to choose the menu option
    no_winners = True
    while no_winners:
        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit \n")
        # ask player to enter choice
        choice = int(input("Choose an option: "))

        # check if choice was a valid integer
        if 1 <= choice <= 4:

            if choice == 1:
                # deal new card
                card = rng.next_int(13) + 1
                # add new card value to player
                if card == 1:
                    print("\nYour card is a ACE!")
                    player_hand += card
                elif 2 <= card <= 10:
                    print(f"\nYour card is a {card}!")
                    player_hand += card
                elif card == 11:
                    print("\nYour card is a JACK!")
                    card = 10
                    player_hand += card
                elif card == 12:
                    print("\nYour card is a QUEEN!")
                    card = 10
                    player_hand += card
                elif card == 13:
                    print("\nYour card is a KING!")
                    card = 10
                    player_hand += card

                print("Your hand is:", player_hand, "\n")

                # if player_hand is equal to 21
                if player_hand == 21:
                    # set no_winners to be False
                    # print winning messages
                    print("BLACKJACK! You win!\n")
                    # track the num. of games player wins
                    player_wins += 1
                    no_winners = False
                # else if player_hand is greater than 21 (Bust)
                elif player_hand > 21:
                    # do something similar in the
                    print("You exceeded 21! You lose.\n")
                    dealer_wins += 1
                    no_winners = False

            elif choice == 2:
                # deal a card in [16, 26] to the dealer
                dealer_hand = rng.next_int(11) + 16

                print(f"\nDealer's hand: {dealer_hand}")
                print(f"Your hand is: {player_hand} \n")
                # compare dealer hand with player
                # determine the winner
                if dealer_hand == player_hand:
                    print("It's a tie! No one wins! \n")
                    tie_games += 1
                    no_winners = False
                elif dealer_hand > 21:
                    print("You win! \n")
                    player_wins += 1
                    no_winners = False
                elif (21 - dealer_hand) < (21 - player_hand):
                    print("Dealer wins! \n")
                    dealer_wins += 1
                    no_winners = False
                elif dealer_hand == 21:
                    print("Dealer wins! \n")
                    dealer_wins += 1
                    no_winners = False
                elif (21 - dealer_hand) > (21 - player_hand):
                    print("You win! \n")
                    player_wins += 1
                    no_winners = False

            elif choice == 3:
                # print stats, using the prev. declared variables
                print(f"\nNumber of Player wins: {player_wins}")
                print(f"Number of Dealer wins: {dealer_wins}")
                print(f"Number of tie games: {tie_games}")
                print(f"Total # of games played is: {game_num - 1}")
                print(f"Percentage of Player wins: {100 * (player_wins / (game_num - 1))}%\n")

            elif choice == 4:
                # end the game by terminating the first while loop
                no_winners = False
                game_continue = False

        else:
            # if the user does not input a valid choice
            print("\nInvalid input!")
            print("Please enter an integer value between 1 and 4.\n")
            # very important! This make's sure that the user gets prompted to make another choice,
            # but also prevents starting a whole new game.
            continue
