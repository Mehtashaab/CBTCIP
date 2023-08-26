def game_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Game is  tie!"
    elif player_choice == "rock":
        if computer_choice == "paper":
            return "Computer wins!"
        else:
            return "Player wins!"
    elif player_choice == "paper":
        if computer_choice == "scissor":
            return "Computer wins!"
        else:
            return "Player wins!"
    elif player_choice == "rock":
        if computer_choice == "scissor":
            return "Player wins!"
        else:
            return "Computer wins!"
    
    elif player_choice == "scissor":
        if computer_choice == "rock":
            return "Computer wins!"
        else:
            return "Player wins!"
    else:
        return "Invalid input. Please choose rock, paper, or scissor."

import random

def start_game():
    choices = ["rock", "paper", "scissor"]
    computer_choice = random.choice(choices)
    
    player_choice = input("Enter your choice (rock/paper/scissor): ").lower()
    
    if player_choice in choices:
        print(f"Computer chose {computer_choice}.")
        result = game_winner(player_choice, computer_choice)
        print(result)
    else:
        print("Invalid input. Please choose rock, paper, or scissor.")

def main():
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        start_game()
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

if __name__ == "__main__":
    main()
