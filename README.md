# Grocery-Ordering-System

Grocery Store Checkout System - Updated Features Overview
Project Title: Grocery Store Checkout System (Python Beginner Team Challenge)
Objective: To simulate a real-life grocery store checkout experience using Python, focusing on inventory
management, cart operations, delivery options, and budget handling, all of which align with beginner-tointermediate
Python programming skills.
Updated Features
Product Inventory Management
Each grocery item in the catalog now has a set stock quantity.
When a customer adds an item to the cart, the available quantity is decreased.
If a product is out of stock, the system informs the user that it cannot be added to the cart.
Robust Input Handling with Try-Except Blocks
If a customer enters a product name that does not exist, the system uses try-except to catch the
error.
The program displays a friendly message: "⚠ We do not sell that here. Please choose a product from
the menu."
This prevents the program from crashing due to unexpected input.
Dynamic Cart Operations
The customer can now view their cart and remove items if needed.
Useful in cases where the total cost exceeds the customer’s available budget.
The inventory is automatically updated when items are removed (i.e., stock increases).
Budget Handling and Customer Choices
After checkout, the system compares the total cart value to the customer’s available funds.
If the user has insufficient funds, they are given options:
Add more money to complete the transaction.
Remove items from their cart to lower the total.
Cancel the purchase entirely if neither option is feasible.
Delivery Option Logic
ustomers are asked whether they want their items delivered or not.
If the total food cost exceeds R1000, delivery is free.
If the total is less than R1000, delivery is charged based on weight:
R2 per 500 grams of food.
Charges are calculated proportionally. (Example: 2kg = R8 delivery fee)
This encourages larger purchases and simulates realistic delivery pricing.
Clear Summary and Messaging
The system prints a clear, readable cart summary, total cost, and payment status.
If the transaction is successful, the user receives a thank-you message with their change amount.
If the transaction fails, a friendly exit message is displayed.
Modular and Maintainable Design
The code is broken into functions that handle specific operations such as add_to_cart ,
remove_from_cart , handle_payment , and show_cart .
This makes the logic easy to maintain, understand, and eventually integrate into a Tkinter-based
GUI.
Tkinter GUI Preparation (Future Step)
The current console version is written in a way that can be smoothly ported to a graphical
interface.
Planned features for the GUI include:
Listbox for item selection
Buttons for adding/removing items
Dynamic labels to show cart status and total
Entry fields for user payments
Delivery option selection via checkboxes or radio buttons
Summary This updated system not only meets the original challenge goals but also simulates a realistic
shopping experience by including features like stock tracking, cart adjustments, delivery calculations, and
real-time budget decisions. It aligns perfectly with the Python topics learned so far: functions, conditionals,
loops, data structures (lists/dictionaries), and basic user input/output. With the logic modularized, it is now
ready for GUI enhancement using Tkinter.
Next Steps for Team: - Test all current logic in the console. - Assign GUI components to individual team
members. - Begin designing the GUI layout in Tkinter.
Let’s Build It!
