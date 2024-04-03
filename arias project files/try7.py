import json
import sqlite3
from getpass import getpass
from datetime import datetime
import os

class Budget:
    def __init__(self, user_id, category, amount):
        self.user_id = user_id
        self.category = category
        self.amount = amount

    def deposit(self, amount):
        self.amount += amount
        self.update_budget()
        self.record_transaction(amount, "Deposit")
        return f"Amount deposited successfully. New balance in {self.category} category: ${self.amount}"

    def withdraw(self, amount):
        if amount > self.amount:
            return f"Insufficient funds. Current balance in {self.category} category: ${self.amount}"
        else:
            self.amount -= amount
            self.update_budget()
            self.record_transaction(amount, "Withdrawal")
            return f"Withdrawal successful. New balance in {self.category} category: ${self.amount}"

    def check_balance(self):
        return f"Current balance in {self.category} category: ${self.amount}"

    def update_budget(self):
        # Update budget in the database
        conn = sqlite3.connect('budget.db')
        cursor = conn.cursor()
        cursor.execute("""UPDATE budgets SET amount = ? WHERE user_id = ? AND category = ?""",
                       (self.amount, self.user_id, self.category))
        conn.commit()
        conn.close()

    def record_transaction(self, amount, transaction_type):
        # Record transaction in the database
        conn = sqlite3.connect('budget.db')
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO transactions (user_id, category, amount, transaction_type, timestamp) 
                          VALUES (?, ?, ?, ?, ?)""", (self.user_id, self.category, amount, transaction_type, datetime.now()))
        conn.commit()
        conn.close()


def login():
    while True:
        choice = input("Do you want to (C)reate an account or (L)ogin? ").strip().lower()
        if choice == "c":
            return create_profile()
        elif choice == "l":
            username = input("Enter username: ")
            password = getpass("Enter password: ")

            # Check if profiles.json exists, if not, create an empty file
            if not os.path.exists("profiles.json"):
                with open("profiles.json", "w") as file:
                    json.dump({}, file)

            with open("profiles.json", "r") as file:
                profiles = json.load(file)
                if username in profiles and profiles[username]["password"] == password:
                    return profiles[username]
                else:
                    print("Invalid username or password.")
        else:
            print("Invalid choice. Please enter 'C' to create an account or 'L' to login.")

def create_profile():
    username = input("Enter username: ")
    password = getpass("Enter password: ")
    profile = {"username": username, "password": password}
    with open("profiles.json", "a+") as file:
        file.seek(0)
        profiles = json.load(file)
        if username in profiles:
            print("User already exists.")
            return None
        profile_id = len(profiles) + 1
        profile["id"] = profile_id
        profiles[username] = profile
        file.seek(0)
        json.dump(profiles, file)
    return profile

def main():
    profile = login()
    if profile:
        print(f"Welcome, {profile['username']}!")
        conn = sqlite3.connect('budget.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS budgets 
                          (id INTEGER PRIMARY KEY, user_id INTEGER, category TEXT, amount REAL)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS transactions 
                          (id INTEGER PRIMARY KEY, user_id INTEGER, category TEXT, amount REAL, 
                          transaction_type TEXT, timestamp TEXT)''')
        cursor.execute('''SELECT * FROM budgets WHERE user_id = ?''', (profile["id"],))
        budgets = {row[2]: Budget(row[1], row[2], row[3]) for row in cursor.fetchall()}
        conn.close()

        while True:
            print("\n======= Budget Application =======")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transaction History")
            print("5. Share Budget")
            print("6. Set Reminder")
            print("7. Exit")

            choice = input("\nEnter your choice (1/2/3/4/5/6/7): ")

            if choice == '1':
                category = input("Enter category (Food/Clothing/Entertainment): ").capitalize()
                amount = float(input("Enter amount to deposit: "))
                if category in budgets:
                    print(budgets[category].deposit(amount))
                else:
                    print("Invalid category entered.")

            elif choice == '2':
                category = input("Enter category (Food/Clothing/Entertainment): ").capitalize()
                amount = float(input("Enter amount to withdraw: "))
                if category in budgets:
                    print(budgets[category].withdraw(amount))
                else:
                    print("Invalid category entered.")

            elif choice == '3':
                category = input("Enter category (Food/Clothing/Entertainment): ").capitalize()
                if category in budgets:
                    print(budgets[category].check_balance())
                else:
                    print("Invalid category entered.")

            elif choice == '4':
                category = input("Enter category (Food/Clothing/Entertainment) to view transactions: ").capitalize()
                if category in budgets:
                    conn = sqlite3.connect('budget.db')
                    cursor = conn.cursor()
                    cursor.execute('''SELECT * FROM transactions 
                                      WHERE user_id = ? AND category = ?''', (profile["id"], category))
                    transactions = cursor.fetchall()
                    conn.close()
                    if transactions:
                        print("\nTransaction History:")
                        for transaction in transactions:
                            print(f"{transaction[4]}: ${transaction[3]} ({transaction[5]})")
                    else:
                        print("No transactions found for this category.")
                else:
                    print("Invalid category entered.")

            elif choice == '5':
                print("Feature not yet implemented.")

            elif choice == '6':
                print("Feature not yet implemented.")

            elif choice == '7':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please enter a valid option (1/2/3/4/5/6/7).")

if __name__ == "__main__":
    main()
