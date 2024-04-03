# user_management.py

# Create a dictionary to store user profiles.
user_profiles = {}

# Function to create a new user profile.
def create_user_profile():
    username = input("Enter a username for the new user: ")
    if username not in user_profiles:
        user_profiles[username] = []
        print(f"User profile '{username}' created successfully!")
    else:
        print(f"Username '{username}' already exists. Please choose a different username.")

# Function to associate a rule with a user.
def assign_rule_to_user():
    username = input("Enter the username of the user: ")
    if username in user_profiles:
        rule_title = input("Enter the title of the rule to assign: ")
        if rule_title in rules:
            user_profiles[username].append(rule_title)
            print(f"Rule '{rule_title}' assigned to user '{username}' successfully!")
        else:
            print(f"Rule '{rule_title}' not found in the rule book.")
    else:
        print(f"User '{username}' not found. Create a user profile first.")

# Main program loop.
while True:
    print("\nUser Management Menu:")
    print("1. Create a User Profile")
    print("2. Assign a Rule to a User")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        create_user_profile()
    elif choice == '2':
        assign_rule_to_user()
    elif choice == '3':
        # Save user profiles to a file or database if needed.
        print("Exiting User Management.")
        break
    else:
        print("Invalid choice. Please try again.")
