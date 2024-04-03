import random

def play_game():
    secret_number = random.randint(1, 100)
    guesses_left = 3

    while guesses_left > 0:
        guess = int(input(f"Guess the number between 1 and 100 (You have {guesses_left} guesses left): "))
        
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue  # Skip the rest of the loop and ask for input again
        
        if guess == secret_number:
            print("In the realm of numbers, you took flight,")
            print("With keen perception, you saw the light.")
            print("Your guess was perfect, shining so bright,")
            print(f"In the world of digits, you got it right! {secret_number}. You lit!")
            break
        elif guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")
        
        guesses_left -= 1

    if guesses_left == 0:
        print(f"Sorry, you're out of guesses. The secret number was {secret_number}.")
    
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("End of the game.")

# Start the game
play_game()