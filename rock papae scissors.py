import random
print("Welcome to Rock, Paper, Scissors Game!")

choices = ["rock", "paper", "scissors"]

user = input("Enter your choice (rock, paper, scissors): ").lower()
computer = random.choice(choices)

print("computer:", computer)

# Tie case
if user == computer:
    print("It's a tie!")

# Your winning conditions are:
elif user == "rock" and computer == "scissors":
    print("You win!")

elif user == "paper" and computer == "rock":
    print("You win!")

elif user == "scissors" and computer == "paper":
    print("You win!")

# Computer winning conditions are:
elif computer == "rock" and user == "scissors":
    print("Computer wins!")

elif computer == "paper" and user == "rock":
    print("Computer wins!")

elif computer == "scissors" and user == "paper":
    print("Computer wins!")

    # invalid input 
else:
    print("invalid input")
