# Write your solution below the starter code
# Follow the instructions in the tab to the right
#import random
from random import seed
from random import randint

# Welcome the user to the game
print("Welcome to rock, paper, scissors. Good luck!")

# Make a choice for the computer player
# Assign a random number between 1 and 3 to computer_choice
computer_choice = randint(1, 3)
if computer_choice == 1:
    computer_choice = "rock"
elif computer_choice == 2:
    computer_choice = "paper"
else:
    computer_choice = "scissors"

# Get a choice from the user
user_choice = input("Rock, Paper, or Scissors: ")
# Compare the user and computer choice
if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
    print("The computer choses ", computer_choice)
    print("You have to enter Rock, Paper, or Scissors.")
# Print the right message, based on the choices
elif user_choice == computer_choice:
    print("The computer choses ", computer_choice)
    print(f"{user_choice} and {user_choice}. It's a draw.")
elif user_choice == "rock" and computer_choice == "scissors":
    print("The computer choses ", computer_choice)
    print("Rock smashes Scissors. You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("The computer choses ", computer_choice)
    print("Paper covers Rock. You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("The computer choses ", computer_choice)
    print("Scissors cut Paper. You win!")
elif computer_choice == "rock" and user_choice == "scissors":
    print("The computer choses ", computer_choice)
    print("Rock smashes Scissors. You lose!")
elif computer_choice == "paper" and user_choice == "rock":
    print("The computer choses ", computer_choice)
    print("Paper covers Rock. You lose!")
elif computer_choice == "scissors" and user_choice == "paper":
    print("The computer choses ", computer_choice)
    print("Scissors cut Paper. You lose!")