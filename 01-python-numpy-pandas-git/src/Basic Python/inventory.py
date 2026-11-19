def view_inventory(inventory):
    if not inventory:
        print("\nThere is no item in inventory.")

    else:
        print("\nThe items of inventory are: ")
        item_count = 1
        for items in inventory:
            print(f"{item_count}. {items['name']} - ${items['price']} - Quantity: {items['quantity']}")
            item_count += 1
    print("\n")

def add_items(inventory):
    name = input("\nEnter the name of item you wanted to add: ")
    price = int(input("Enter the price of item: $"))
    quantity = int(input("Enter the amount of item: "))
    inventory.append({"name":name, "price":price, "quantity":quantity})
    print("The item has been successfully added")
    print("\n")

def sell_item(inventory, total_sale):
    name = input("Enter the name of item to sell: ")
    item_found = False
    for items in inventory:
        if items['name'].lower() == name.lower():
            item_found = True
            sell_quantity = int(input("Enter the amount of quantity to sell: "))
            if items['quantity'] >= sell_quantity:
                items['quantity'] -= sell_quantity
                sale_amount = items['price'] * sell_quantity
                total_sale += sale_amount
                print(f"Sold {sell_quantity} {items['name']} for ${sale_amount}\n")
                return total_sale
            else:
                print("Item out of stock.\n")
                return total_sale
    print("No such item is present in inventory.\n")
    return total_sale

inventory_list = []
total_sale = 0
while True:
    print(" ----------Main Menu---------- ")
    print("| 1. View Items               |")
    print("| 2. Add Items                |")
    print("| 3. Sell Item                |")
    print("| 4. View Total Sale          |")
    print("| 5. Exit                     |")
    print(" -----------------------------")
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        view_inventory(inventory_list)
    elif choice == 2:
        add_items(inventory_list)
    elif choice == 3:
        total_sale = sell_item(inventory_list, total_sale)
    elif choice == 4:
        print(f"Total sales are ${total_sale}\n")
    elif choice == 5:
        print("\nExiting the Program....")
        break
    else:
        print("\nEnter the choice between (1-5)")
