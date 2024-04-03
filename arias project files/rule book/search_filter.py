# search_filter.py

# Function to search for a rule by title.
def search_rule_by_title():
    title_to_search = input("Enter the title of the rule you want to find: ")
    found = False
    for category, rules in rule_categories.items():
        for rule in rules:
            if rule['title'] == title_to_search:
                print(f"Category: {category}\nTitle: {rule['title']}\nDescription: {rule['description']}\n")
                found = True
    if not found:
        print(f"Rule '{title_to_search}' not found.")

# Main program loop.
while True:
    print("\nSearch and Filter Menu:")
    print("1. Search for a Rule by Title")
    print("2. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        search_rule_by_title()
    elif choice == '2':
        print("Exiting Search and Filter.")
        break
    else:
        print("Invalid choice. Please try again.")
