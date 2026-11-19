def view_product(product):
    if not product:
        print("\nNo Product available.")
    else:
        item_count = 1
        print("\nThe available products are:")
        for items in product:
            print(f"{item_count}. {items['name']} - ${items['price']:.2f}")
            item_count += 1
    print("\n")

def add_product(product, cart):
    name = input("\nEnter the name of product: ")
    for items in product:
        if name.lower() == items['name'].lower():
            cart.append(items)
            print(f"Product '{name}' added to cart successfully.\n")
            return
    print(f"No product named '{name} found.\n")
    print("\n")

def cart_products(cart):
    if not cart:
        print("\nNo product was added to cart.")
    else:
        item_count = 1
        print("\nAvailable products in cart are:")
        for items in cart:
            print(f"{item_count}. {items['name']} - ${items['price']:.2f}")
            item_count += 1
    print("\n")

def remove_product_from_cart(cart):
    if not cart:
        print("\nNo product was added to cart.")
    else:
        name = input("\nEnter the name of product to remove from cart: ")
        for items in cart:
            if name.lower() == items['name'].lower():
                cart.remove(items)
                print("Product removed from cart successfully.\n")
                return
        print(f"No product named {name} found in the cart list.")
    print("\n")

def checkout(cart):
    if not cart:
        print("\nYour cart is empty")
    else:
        total_price = 0.00
        for items in cart:
            total_price += items['price']
        print("\nCheckout Summary:")
        item_count = 1
        for items in cart:
            print(f"{item_count}. {items['name']} - ${items['price']:.2f}")
            item_count += 1
        print(f"Total price is {total_price:.2f}")
        print("Thank you for shopping....")
        cart.clear()
    print("\n")

product_list = [{"name":"Sneakers", "price":15.5},
                {"name":"Leather bag", "price":20},
                {"name":"Hoodie", "price":19.5},
                {"name":"Watch", "price":10},
                {"name":"Glasses","price":5.5}]
cart_list = []
print(f"{'Welcome to Ecommerce Website!!!':^145}")
while True:
    print(" ----------Main Menu---------- ")
    print("| 1. View Products            |")
    print("| 2. Add Product to Cart      |")
    print("| 3. Show Cart                |")
    print("| 4. Remove Product From Cart |")
    print("| 5. Checkout                 |")
    print("| 6. Exit                     |")
    print(" -----------------------------")
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        view_product(product_list)
    elif choice == 2:
        add_product(product_list, cart_list)
    elif choice == 3:
        cart_products(cart_list)
    elif choice == 4:
        remove_product_from_cart(cart_list)
    elif choice == 5:
        checkout(cart_list)
    elif choice == 6:
        print("\nEnding Program...")
        break
    else:
        print("Please enter the choice between (1-4)")
