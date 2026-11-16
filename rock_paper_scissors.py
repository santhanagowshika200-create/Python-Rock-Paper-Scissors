import random

def get_user_choice():
    """Prompt the user for a valid choice or exit command."""
    valid_choices = {
        '1': 'rock',
        'rock': 'rock',
        'r': 'rock',
        '2': 'paper',
        'paper': 'paper',
        'p': 'paper',
        '3': 'scissors',
        'scissors': 'scissors',
        's': 'scissors',
        '4': 'exit',
        'exit': 'exit',
        'q': 'exit',
        'quit': 'exit'
    }

    while True:
        print("\nChoose an option:")
        print("1. Rock (r)")
        print("2. Paper (p)")
        print("3. Scissors (s)")
        print("4. Exit (q)")

        user_input = input("Enter your choice: ").strip().lower()

        if user_input in valid_choices:
            return valid_choices[user_input]
        else:
            print("Invalid input. Please choose 1, 2, 3, or 4 (or type rock, paper, scissors, exit).")

def get_computer_choice():
    """Randomly select Rock, Paper, or Scissors for the computer."""
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

def determine_winner(user_choice, computer_choice):
    """Compare choices and return 'user', 'computer', or 'draw'."""
    if user_choice == computer_choice:
        return 'draw'

    # Dictionary mapping each choice to the choice it defeats
    winning_rules = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }

    if winning_rules[user_choice] == computer_choice:
        return 'user'
    else:
        return 'computer'

def play_game():
    """Main game loop to run multiple rounds and track scores."""
    user_score = 0
    computer_score = 0
    ties = 0
    round_number = 1

    print("========================================")
    print("        ROCK - PAPER - SCISSORS         ")
    print("========================================")

    while True:
        print(f"\n--- Round {round_number} ---")
        user_choice = get_user_choice()

        # Check if the user chose to exit the game
        if user_choice == 'exit':
            break

        computer_choice = get_computer_choice()

        print(f"\nYou chose:      {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

        # Determine round winner and update scores
        winner = determine_winner(user_choice, computer_choice)

        if winner == 'user':
            print("Result: You win this round!")
            user_score += 1
        elif winner == 'computer':
            print("Result: Computer wins this round!")
            computer_score += 1
        else:
            print("Result: It's a draw!")
            ties += 1

        # Display current scoreboard
        print(f"Score -> You: {user_score} | Computer: {computer_score} | Draws: {ties}")
        round_number += 1

    # Display final summary when exiting
    print("\n========================================")
    print("               FINAL SCORE              ")
    print("========================================")
    print(f"Your Score:     {user_score}")
    print(f"Computer Score: {computer_score}")
    print(f"Draws:          {ties}")

    if user_score > computer_score:
        print("\nCongratulations! You won the match!")
    elif computer_score > user_score:
        print("\nComputer won the match. Better luck next time!")
    else:
        print("\nThe match ended in a tie!")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()