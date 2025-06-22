# 🛒 Grocery Ordering System

### ✅ Project Overview
A beginner-friendly Python project that simulates a real-life grocery store checkout system. It handles inventory, budget management, delivery logic, and cart operations — giving a feel of what a real ordering system might involve.

---

### 🧠 Key Features

#### 🗃️ Product Inventory Management
- Each item has a stock quantity.
- Stock updates automatically when items are added/removed.
- Out-of-stock items cannot be selected.

#### 🔒 Input Handling
- Prevents app crashes with `try-except` blocks.
- Gives friendly messages for invalid input like:  
  _"⚠ We do not sell that here. Please choose a product from the menu."_

#### 🛍️ Dynamic Cart Operations
- View and edit cart anytime.
- Remove items to adjust total.
- Stock updates dynamically with cart changes.

#### 💸 Budget Handling
- Not enough money? Choose to:
  - Add more funds
  - Remove items
  - Cancel purchase

#### 🚚 Delivery Logic
- Free delivery for orders **R1000+**.
- Below R1000? Delivery charged by weight at **R2 per 500g**.
- Proportional calculation (e.g., 2kg = R8).

#### 💬 Clear Summaries & Feedback
- Readable cart, total, and payment info.
- Confirmation messages for successful and failed transactions.

---

### 🧩 Code Structure

Modular design with clearly defined functions:
- `add_to_cart()`
- `remove_from_cart()`
- `handle_payment()`
- `show_cart()`

Easily extendable into a GUI using **Tkinter** in future versions.

---

### 🚀 Future Plans
- Migrate logic into a Tkinter GUI.
- Features to include:
  - Item selection via Listbox
  - Buttons to modify cart
  - Labels for totals
  - Entry fields for payment
  - Delivery options via checkboxes or radio buttons

---

### 📌 Summary

This Grocery Ordering System helped me reinforce:
- Functions
- Loops and conditionals
- Lists and dictionaries
- Handling user input
- Real-world logic like stock, payments, and delivery

It was also a lesson in simplicity — learning to break down problems into small, manageable steps and stop overthinking.

---

### 🔗 Project Repository
Explore the full code here:  
📍 [Grocery Ordering System on GitHub](https://github.com/bongumusa-web/Grocery-Ordering-System/blob/main/Main_grocery_ordering_system.py)

---

### 🔖 Hashtags (for ALX task submission)
`#ALX_SE` `#ALX_PDBE` `#ALX_PDFE` `#ALX_FE` `#ALX_BE`  
Mention: [@alx_africa](https://twitter.com/alx_africa)

---

### 🧠 Lesson Learned
Overthinking led to big, unnecessary code. But by following instructions, breaking things down, and using ChatGPT + YouTube for help — I’ve learned to **code smarter, not harder**.

Let's keep building! 💪
