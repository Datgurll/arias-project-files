# rule_categories.py

# Create a dictionary to store rules with categories.
rule_categories = {}

# Function to add a new rule to a specific category.
def add_rule_to_category():
    category = input("Enter the category for the new rule: ")
    if category not in rule_categories:
        rule_categories[category] = []
    rule_title = input("Enter the title of the new rule: ")
    rule_description = input("Enter the description of the new rule: ")
    rule_categories[category].append({'title': rule_title, 'description': rule_description})
    print(f"Rule '{rule_title}' added to the '{category}' category successfully!")

# Function to view rules by category.
def view_rules_by_category():
    if not rule_categories:
        print("No rules have been categorized yet.")
    else:
        print("\n--- Rule Categories ---")
        for category, rules in rule_categories.items():
            print(f"\nCategory: {category}")
            for rule in rules:
                print(f"Title: {rule['title']}\nDescription: {rule['description']}\n")

# Main program loop.
while True:
    print("\nRule Categories Menu:")
    print("1. Add a New Rule to a Category")
    print("2. View Rules by Category")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_rule_to_category()
    elif choice == '2':
        view_rules_by_category()
    elif choice == '3':
        # Save the categorized rules to a file or database if needed.
        print("Exiting Rule Categories.")
        break
    else:
        print("Invalid choice. Please try again.")
