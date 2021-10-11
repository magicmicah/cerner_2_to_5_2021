# cerner_2tothe5th_2021
# I want to play a game. Rock paper scissors in under 32 lines of code. 
import random, os
computer_score = 0; player_score = 0; playing = True
while playing is True:
    print(f"Computer score: {computer_score} \nPlayer score: {player_score}")
    player_choice = input("Rock, paper, scissors?\n")
    rps_list = ["rock", "paper", "scissors"]
    if (player_choice.lower() in rps_list): player_choice = player_choice.lower()
    elif (player_choice.lower() == "scissor"): player_choice = player_choice.lower()
    else:
        print("Not a choice. Try again.")
    computer_chance= random.randint(0, len(rps_list)-1)
    computer_choice = rps_list[computer_chance]
    print(f"Player has picked {player_choice} and computer has picked {computer_choice}.")
    if (computer_choice == player_choice): print(f"We both picked {computer_choice}. Play again.")
    elif (computer_choice == "rock"):
        if(player_choice == "scissors"): print("You lose"); computer_score = computer_score + 1;
        else: print("You win"); player_score = player_score + 1
    elif (computer_choice == "paper"):
        if(player_choice == "rock"): print("You lose"); computer_score = computer_score + 1;
        else: print("You win"); player_score = player_score + 1
    elif (computer_choice == "scissors"):
        if(player_choice == "paper"): print("You lose"); computer_score = computer_score + 1;
        else: print("You win"); player_score = player_score + 1
    play_again = input("Press enter to play again\n")
    if (play_again == ""):
        if(os.name == 'nt'): os.system('cls')
        else: os.system('clear')
    else: playing = False; print("Thanks for playing.")
