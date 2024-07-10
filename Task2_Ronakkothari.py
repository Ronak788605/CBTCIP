import random

def generate_number(length=4):
    return ''.join(random.choices('0123456789', k=length))

def get_feedback(secret, guess):
    correct_position = sum(s == g for s, g in zip(secret, guess))
    correct_number = sum(min(secret.count(d), guess.count(d)) for d in set(guess))
    return correct_position, correct_number - correct_position

def play_round(secret):
    attempts = 0
    while True:
        guess = input("Enter your guess: ")
        attempts += 1
        if guess == secret:
            print("Congratulations! You've guessed the number!")
            return attempts
        correct_position, correct_number = get_feedback(secret, guess)
        print(f"Correct numbers in correct positions: {correct_position}")
        print(f"Correct numbers in wrong positions: {correct_number}")

def mastermind_game():
    print("Player 1 sets the number.")
    player1_number = input("Player 1, enter your secret number: ")
    
    print("\nPlayer 2, it's your turn to guess.")
    player2_attempts = play_round(player1_number)
    
    print("\nPlayer 2 sets the number.")
    player2_number = input("Player 2, enter your secret number: ")
    
    print("\nPlayer 1, it's your turn to guess.")
    player1_attempts = play_round(player2_number)
    
    print("\nGame Over")
    if player1_attempts < player2_attempts:
        print("Player 1 wins and is crowned Mastermind!")
    else:
        print("Player 2 wins and is crowned Mastermind!")

if __name__ == "__main__":
    mastermind_game()
