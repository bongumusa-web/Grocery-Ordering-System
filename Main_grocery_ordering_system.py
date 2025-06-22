from shopping import display_menu, select_items, view_cart, checkout


def main():
    print("************** MENU **************")
    display_menu()

    print("************** ORDER **************")
    cart = select_items()

    print("************** CART **************")
    item_total, delivery_total = view_cart(cart)
    print(f"Total: R{item_total:.2f}, Delivery: R{delivery_total:.2f}")

    checkout(cart, item_total, delivery_total)


if __name__ == "__main__":
    main()
