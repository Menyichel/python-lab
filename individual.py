import random

print("Welcome to Rock, Paper, Scissors!")

user_wins = 0
computer_wins = 0
draws = 0

while True:
    print("Enter your choice (rock, paper, scissors):")
    user_choice = input()

    computer_choice = random.choice(["rock", "paper", "scissors"])

    if user_choice == computer_choice:
        print("It's a draw!")
        draws += 1
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win! Rock beats scissors.")
        user_wins += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win! Paper beats rock.")
        user_wins += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win! Scissors beats paper.")
        user_wins += 1
    else:
        print("The computer wins! {} beats {}.".format(computer_choice, user_choice))
        computer_wins += 1

    print("Do you want to play again? (yes/no)")
    play_again = input()
    if play_again == "no":
        break

print("Thanks for playing! Here are the statistics:")
print("User wins:", user_wins)
print("Computer wins:", computer_wins)
print("Draws:", draws)