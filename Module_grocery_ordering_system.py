import math

menu_dict = {
    1: ["milk 500ml", 20, 10, 515], # item, quantity, price, weight in grams
    2: ["milk 1l", 10, 20, 1030],
    3: ["coke 500ml", 10, 11, 500],
    4: ["fanta 500ml", 11, 10, 500],
    5: ["stony 500ml", 3, 10, 500],
    6: ["sprite 500ml", 7, 10, 500],
    7: ["coke 1l", 50, 18, 1000],
    8: ["fanta 1l", 13, 16, 1000],
    9: ["stony 1l", 15, 16, 1000],
    10: ["sprite 1l", 18,  16, 1000],
    11: ["cheese slice", 20, 3, 28],
    12: ["eggs 6 pack", 33, 14, 348],
    13: ["rama 500g", 15,  13, 500],
    14: ["russian 60g", 60, 8, 60],
    15: ["arch 500g", 14, 50, 500],
    16: ["sugar 500g", 60, 14, 500],
    17: ["frisco 200g", 55,  23, 200],
    18: ["fries 71g", 13,  10, 71],
    19: ["fries 117g", 32, 16, 117],
    20: ["fries 190g", 10, 16, 1000],
}

def display_menu():
    for key, item in menu_dict.items():
        print(f"{key}. {item[0]} - R{item[2]}")

def select_items():
    cart = []
    while True:
        try:
            choice = int(input("Enter item number (0 to finish): "))
            if choice == 0:
                break
            if choice not in menu_dict:
                print("Invalid item number.")
                continue
            name, stock, price, weight = menu_dict[choice]
            qty = int(input(f"Enter quantity of {name}: "))
            if qty > stock:
                print(f"Only {stock} available.")
                continue
            menu_dict[choice][1] -= qty
            total_price = qty * price
            delivery_cost = round((weight * qty) * (2 / 200), 2)
            cart.append([choice, name, price, qty, total_price, delivery_cost])
            print(f"Added {qty} x {name}")
        except ValueError:
            print("Please enter a valid number.")
    return cart

def view_cart(cart):
    item_total = 0
    delivery_total = 0
    for _, name, price, qty, total, delivery in cart:
        print(f"{name} - R{price} x {qty} = R{total:.2f} | Delivery: R{delivery:.2f}")
        item_total += total
        delivery_total += delivery
    return item_total, delivery_total

def checkout(cart, item_total, delivery_total):
    confirm = input("Proceed to payment? (yes/no): ").lower()
    if confirm != "yes":
        print("Checkout cancelled.")
        return

    while True:
        try:
            amount_paid = float(input("Enter amount to pay: "))
            if amount_paid >= item_total:
                break
            print(f"Insufficient. You need R{item_total - amount_paid:.2f} more.")
            option = input("Add more money (1) or remove items (2)? ")
            if option == "1":
                continue
            elif option == "2":
                remove_items(cart)
                item_total, delivery_total = view_cart(cart)
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")

    handle_delivery(cart, amount_paid, item_total, delivery_total)

def remove_items(cart):
    while True:
        print("\nYour cart:")
        for idx, (_, name, _, qty, total, _) in enumerate(cart):
            print(f"{idx+1}. {name} - Qty: {qty} | Total: R{total:.2f}")
        try:
            i = int(input("Enter item number to remove (0 to cancel): ")) - 1
            if i == -1:
                break
            item = cart[i]
            remove_qty = int(input(f"How many '{item[1]}' to remove? (Max: {item[3]}): "))
            if 0 < remove_qty <= item[3]:
                item[3] -= remove_qty
                item[4] = item[3] * item[2]
                item[5] = round((item[3] * menu_dict[item[0]][3]) * (2 / 200), 2)
                menu_dict[item[0]][1] += remove_qty
                if item[3] == 0:
                    cart.pop(i)
                print("Item updated.")
            else:
                print("Invalid quantity.")
        except (ValueError, IndexError):
            print("Invalid choice.")

def handle_delivery(cart, amount_paid, item_total, delivery_total):
    if item_total >= 1000:
        print(f"Change: R{amount_paid - item_total:.2f} | Free delivery.")
        return

    option = input("Do you want delivery? (yes/no): ").lower()
    if option != "yes":
        print(f"Change: R{amount_paid - item_total:.2f} | Please collect in store.")
        return

    while True:
        try:
            delivery_paid = float(input(f"Delivery fee is R{delivery_total:.2f}. Enter amount: "))
            if delivery_paid >= delivery_total:
                change = (amount_paid - item_total) + (delivery_paid - delivery_total)
                print(f"Change: R{change:.2f}. Delivery confirmed.")
                return
            else:
                print(f"Short by R{delivery_total - delivery_paid:.2f}")
                choice = input("Add more (1) or cancel delivery and collect (2)? ")
                if choice == "1":
                    continue
                elif choice == "2":
                    change = amount_paid - item_total + delivery_paid
                    print(f"Change: R{change:.2f}. Please collect your items in store.")
                    return
        except ValueError:
            print("Invalid input.")
