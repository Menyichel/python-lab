import random

"""
EMANDA GIRMA
ID NO 1176/12
"""

# Initialize the win counts
user_wins = 0
computer_wins = 0
draws = 0

while True:
    # Get the user's choice
    user_choice = input("Please select one Choose rock, paper, or scissors: ")

    # Get the computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    print("Computer choose:" +computer_choice)
  
    # Compare the choices and update the win counts
    if user_choice == computer_choice:
        draws += 1
        print("It's a draw!")
    elif user_choice == "rock" and computer_choice == "scissors":
        user_wins += 1
        print("You win! Rock beats scissors.")
    elif user_choice == "paper" and computer_choice == "rock":
        user_wins += 1
        print("You win! Paper beats rock.")
    elif user_choice == "scissors" and computer_choice == "paper":
        user_wins += 1
        print("You win! Scissors beats paper.")
    else:
        computer_wins += 1
        print("Computer wins.")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

# Print the final statistics
print("\nStatistics:")
print(f"User wins: {user_wins}")
print(f"Computer wins: {computer_wins}")
print(f"Draws: {draws}")
