import random

def get_difficulty_level():
    print("Choose your difficulty level:")
    print("1. Easy (1-50, Unlimited guesses)")
    print("2. Medium (1-100, 10 guesses)")
    print("3. Hard (1-200, 5 guesses)")
    difficulty = input("Enter your choice (1, 2, or 3): ").strip()
    return difficulty

def set_game_parameters(difficulty):
    parameters = {
        '1': {'range_start': 1, 'range_end': 50, 'guesses': float('inf')},  # Unlimited guesses for easy mode
        '2': {'range_start': 1, 'range_end': 100, 'guesses': 10},
        '3': {'range_start': 1, 'range_end': 200, 'guesses': 5},
    }
    return parameters.get(difficulty, parameters['2'])  # Default to medium if invalid

def play_game():
    difficulty = get_difficulty_level()
    game_settings = set_game_parameters(difficulty)
    secret_number = random.randint(game_settings['range_start'], game_settings['range_end'])
    guesses_left = game_settings['guesses']

    print(f"Guess the number between {game_settings['range_start']} and {game_settings['range_end']}.")

    while guesses_left > 0:
        try:
            guess = int(input(f"You have {guesses_left} guesses left. Enter your guess: "))
        except ValueError:
            print("That's not a valid number. Please try again.")
            continue

        if guess < game_settings['range_start'] or guess > game_settings['range_end']:
            print(f"Please enter a number between {game_settings['range_start']} and {game_settings['range_end']}.")
            continue

        if guess == secret_number:
            print("Congratulations! You've guessed the secret number!")
            break
        elif guess < secret_number:
            print("Higher.")
        else:
            print("Lower.")
        
        guesses_left -= 1
        if guesses_left == 0:
            print(f"Sorry, you're out of guesses. The secret number was {secret_number}.")

    if input("Do you want to play again? (yes/no): ").lower() == "yes":
        play_game()
    else:
        print("Thanks for playing. Goodbye!")

# Start the game
if __name__ == "__main__":
    play_game()
