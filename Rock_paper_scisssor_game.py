import random

# Function to get the computer's choice randomly from "rock", "paper", or "scissors"
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner of the game
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    # Conditions for when the user wins
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    # If it's not a tie and the user doesn't win, the user loses
    return "You lose!"

# Function to play the game
def play_game():
    # Get the user's choice and ensure it's valid
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid choice. Enter your choice (rock, paper, or scissors): ").lower()
    
    # Get the computer's choice
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    # Determine and display the winner
    print(determine_winner(user_choice, computer_choice))
    
    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    while play_again not in ["yes", "no"]:
        play_again = input("Invalid choice. Do you want to play again? (yes/no): ").lower()
    
    # If the user wants to play again, call the play_game function again
    if play_again == "yes":
        play_game()

# Start the game
play_game()
