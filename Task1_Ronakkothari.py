import random

def taking_user_choice():
    user_choice = input("Enter your choice (rock,paper or scissors): ")
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter either 'rock', 'paper', or 'scissors'.")
        user_choice = input("Enter your choice (rock/paper/scissors): ")
    return user_choice

def taking_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def taking_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            return "Computer wins!"
        else:
            return "You win!"
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            return "Computer wins!"
        else:
            return "You win!"
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            return "Computer wins!"
        else:
            return "You win!"

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    while True:
        user_choice = taking_user_choice()
        computer_choice = taking_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(taking_winner(user_choice, computer_choice))
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again != 'yes':
            break
    print("Thanks for playing!")

# Start the game
play_game()