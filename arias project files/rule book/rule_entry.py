# rule_entry.py

# Initialize an empty dictionary to store rules.
rules = {}

# Function to add a new rule to the rule book.
def add_rule():
    rule_title = input("Enter the title of the new rule: ")
    rule_description = input("Enter the description of the new rule: ")
    
    # Add the rule to the dictionary.
    rules[rule_title] = rule_description
    print(f"Rule '{rule_title}' added successfully!")

# Function to view all rules in the rule book.
def view_rules():
    if not rules:
        print("The rule book is empty.")
    else:
        print("\n--- Rule Book ---")
        for title, description in rules.items():
            print(f"Title: {title}\nDescription: {description}\n")

# Function to delete a rule from the rule book.
def delete_rule():
    if not rules:
        print("The rule book is empty.")
    else:
        rule_title = input("Enter the title of the rule you want to delete: ")
        if rule_title in rules:
            del rules[rule_title]
            print(f"Rule '{rule_title}' has been deleted.")
        else:
            print(f"Rule '{rule_title}' not found in the rule book.")

# Function to edit a rule in the rule book.
def edit_rule():
    if not rules:
        print("The rule book is empty.")
    else:
        rule_title = input("Enter the title of the rule you want to edit: ")
        if rule_title in rules:
            new_description = input(f"Enter the new description for rule '{rule_title}': ")
            rules[rule_title] = new_description
            print(f"Rule '{rule_title}' has been updated.")
        else:
            print(f"Rule '{rule_title}' not found in the rule book.")

# Main program loop.
while True:
    print("\nRule Entry Menu:")
    print("1. Add a New Rule")
    print("2. View Rules")
    print("3. Delete a Rule")
    print("4. Edit a Rule")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_rule()
    elif choice == '2':
        view_rules()
    elif choice == '3':
        delete_rule()
    elif choice == '4':
        edit_rule()
    elif choice == '5':
        # Save the rules to a file or database if needed.
        print("Exiting Rule Entry.")
        break
    else:
        print("Invalid choice. Please try again.")
3