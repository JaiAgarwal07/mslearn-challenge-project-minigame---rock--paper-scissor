#creating a Rock paper scissors game using python language

# import random module for generating the random choices from players 
print("Welcome to the rock paper and scissors game ")
import random 

# create a list of options
options = ["rock", "paper", "scissors"]

# create the score and round played variables
score = 0
rounds_played = 0

# create the loop to play the game

while True:

    # choose a random option of the list
    computer_choice = random.choice(options)

    # asking for the user input
    player_choice = input("Rock, paper or scissors? \n")

    # if player chooses rock 
    if player_choice.lower() == "rock":
        if computer_choice == "rock":
            print("Computer choose rock. It's a tie!")
        elif computer_choice == "paper":
            print("Computer choose paper. You lose!")
        elif computer_choice == "scissor":
            print("Computer chose scissor. You win!")
            score += 1
        rounds_played += 1

    # if player chose paper
    elif player_choice.lower() == "paper":
        if computer_choice == "rock":
            print("Computer chose rock. You win!")
            score += 1
        elif computer_choice == "paper":
            print("Computer chose paper. It's a tie!")
        elif computer_choice == "scissors":
            print("Computer chose scissors. You lose!")
        rounds_played += 1

    # if player chose scissors
    elif player_choice.lower() == "scissors":
        if computer_choice == "rock":
            print("Computer chose rock. You lose!")
        elif computer_choice == "paper":
            print("Computer chose paper. You win!")
            score += 1
        elif computer_choice == "scissors":
            print("Computer chose scissors. It's a tie!")
        rounds_played += 1

    # if player chose something else
    else:
        print("That's not a valid choice . Please Try Again!")

    # ask the user if they want to play again and break the loop if they don't
    # if they break the loop, print the score
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() == "n":
        print(f"You played {rounds_played} rounds and got {score} points!")
        break
