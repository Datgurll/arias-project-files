import random

# List of words for the game
word_list = ["python", "hangman", "programming", "computer", "coding", "developer", "challenge"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to initialize the game for 1 player
def initialize_single_player_game():
    word_to_guess = choose_word()
    word_length = len(word_to_guess)
    guessed_letters = []
    attempts = 6  # Number of incorrect guesses allowed

    return word_to_guess, word_length, guessed_letters, attempts

# Function to initialize the game for 2 players
def initialize_two_player_game():
    word_to_guess = input("Player 1, enter a word for Player 2 to guess: ").lower()
    word_length = len(word_to_guess)
    guessed_letters = []
    attempts = 6  # Number of incorrect guesses allowed

    return word_to_guess, word_length, guessed_letters, attempts

# Function to display the current state of the word with underscores for unrevealed letters
def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

# Function to play the Hangman game
def play_hangman():
    print("Welcome to Hangman!")
    game_mode = input("Choose a game mode (1 player or 2 player): ").lower()

    if game_mode == "1 player":
        word_to_guess, word_length, guessed_letters, attempts = initialize_single_player_game()
        player_turn = 1
    elif game_mode == "2 player":
        word_to_guess, word_length, guessed_letters, attempts = initialize_two_player_game()
        player_turn = 2
    else:
        print("Invalid game mode. Please choose 1 player or 2 player.")
        return
    
    while attempts > 0:
        print("\nWord:", display_word(word_to_guess, guessed_letters))
        print("Attempts left:", attempts)
        print("Player {}'s turn".format(player_turn))
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word_to_guess:
            print("Correct guess!")
        else:
            print("Incorrect guess.")
            attempts -= 1
        
        if "_" not in display_word(word_to_guess, guessed_letters):
            print("\nPlayer {} wins! The word was: {}".format(player_turn, word_to_guess))
            break

        # Switch to the other player's turn (only for 2-player mode)
        if game_mode == "2 player":
            player_turn = 3 - player_turn  # Toggle between players 1 and 2
    
    if attempts == 0:
        print("\nOut of attempts. It's a draw. The word was:", word_to_guess)

# Main game loop
if __name__ == "__main__":
    while True:
        play_hangman()
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != "yes":
            break
