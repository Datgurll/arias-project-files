def ask_riddle(question, valid_answers):
    answer = input(question + ' ').strip().lower()
    return answer in [a.lower() for a in valid_answers]

if __name__ == "__main__":
    print("Meet Aria: A pretty girl who loves ponytails and braids.")
    print("She was born in a big town called Houston, a curious child who loved exploring and nature.")
    print("Her favorite climate is hot, although she sometimes enjoys the cold as well.")
    print("As she grew up, her fascination turned into a passion for exploring.")
    print("Through streets, beaches, forests, mountains, and deserts she roamed.")
    print("\nOne unpleasant day, she came across a creepy tunnel.")
    print("On the tunnel wall was a note saying, 'Riddles that promised untold treasures.'")
    print("Aria took a deep breath and decided to solve the riddles.")

    lives = 3

    print("\nAria was walking down the tunnel and saw 3 different tunnels. She didn't know which tunnel to go through.")
    if ask_riddle("The 1st tunnel was very cold. The 2nd tunnel was very hot. The 3rd tunnel was warm but the ground was burning hot. Which tunnel does Aria go in?", ["1st", "the 1st tunnel", "first", "the first tunnel"]):
        print("Correct!")
    else:
        print("Wrong! You have lost a life.")
        lives -= 1

    print("\nAfter choosing the correct tunnel, Aria finds a room filled with doors of different colors.")
    if ask_riddle("There's a red door, a blue door, and a green door. The red door leads to a dragon, the blue door leads to an endless ocean, and the green door leads to a meadow. Which door does Aria choose?", ["green", "the green door"]):
        print("Correct!")
    else:
        print("Wrong! You have lost a life.")
        lives -= 1

    print("\nAria found a treasure that says 'Look for the key'. She looks around for the key but can't seem to find it. She keeps looking and finds a mysterious key on the ground. It doesn't go to the treasure, so Aria keeps looking and finds a door.")
    if ask_riddle("Does Aria go through the door or does she look for another key?", ["door", "aria goes through the door", "she goes through the door"]):
        print("Correct!")
    else:
        print("Wrong! You have lost a life.")
        lives -= 1

    if lives > 0:
        print("\nCongratulations, you've completed the game!")
    else:
        print("\nSorry, you've lost all your lives. Game Over.")
