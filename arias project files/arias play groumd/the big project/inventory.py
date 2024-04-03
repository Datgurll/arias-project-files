class InventoryItem:
    def __init__(self, item_id, name, quantity, price):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_id):
        item = next((i for i in self.items if i.item_id == item_id), None)
        if item:
            self.items.remove(item)
        else:
            print(f"Item with ID {item_id} not found.")

    def update_quantity(self, item_id, new_quantity):
        item = next((i for i in self.items if i.item_id == item_id), None)
        if item:
            item.quantity = new_quantity
        else:
            print(f"Item with ID {item_id} not found.")

    def list_items(self):
        for item in self.items:
            print(f"ID: {item.item_id}, Name: {item.name}, Quantity: {item.quantity}, Price: ${item.price:.2f}")


def main():
    my_inventory = Inventory()

    while True:
        print("\nInventory Management Menu:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Quantity")
        print("4. List Items")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item_id = input("Enter item ID: ")
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            item = InventoryItem(item_id, name, quantity, price)
            my_inventory.add_item(item)
            print("Item added to inventory.")

        elif choice == "2":
            item_id = input("Enter item ID to remove: ")
            my_inventory.remove_item(item_id)

        elif choice == "3":
            item_id = input("Enter item ID to update: ")
            new_quantity = int(input("Enter new quantity: "))
            my_inventory.update_quantity(item_id, new_quantity)

        elif choice == "4":
            print("\nInventory List:")
            my_inventory.list_items()

        elif choice == "5":
            print("Exiting Inventory Management.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


