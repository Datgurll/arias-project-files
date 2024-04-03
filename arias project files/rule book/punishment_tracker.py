# punishment_tracker.py

# Create a dictionary to track punishments for each user and rule.
punishments = {}

# Function to apply a punishment to a user for a specific rule.
def apply_punishment():
    username = input("Enter the username of the user: ")
    if username in user_profiles:
        rule_title = input("Enter the title of the rule for the punishment: ")
        if rule_title in rules:
            duration = int(input(f"Enter the duration (in days) of the punishment for '{rule_title}': "))
            if username not in punishments:
                punishments[username] = {}
            punishments[username][rule_title] = duration
            print(f"Punishment applied to user '{username}' for '{rule_title}' for {duration} days.")
        else:
            print(f"Rule '{rule_title}' not found in the rule book.")
    else:
        print(f"User '{username}' not found. Create a user profile first.")

# Function to track and update punishments.
def track_punishments():
    for username, user_punishments in punishments.items():
        for rule_title in list(user_punishments.keys()):
            user_punishments[rule_title] -= 1
            if user_punishments[rule_title] <= 0:
                del user_punishments[rule_title]
                print(f"Punishment for user '{username}' for '{rule_title}' has ended.")

# Main program loop.
while True:
    print("\nPunishment Tracker Menu:")
    print("1. Apply Punishment")
    print("2. Track and Update Punishments")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        apply_punishment()
    elif choice == '2':
        track_punishments()
    elif choice == '3':
        # Save punishment data to a file or database if needed.
        print("Exiting Punishment Tracker.")
        break
    else:
        print("Invalid choice. Please try again.")
