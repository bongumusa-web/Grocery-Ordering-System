<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Grocery Ordering System</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 900px;
      margin: auto;
      padding: 20px;
      line-height: 1.6;
      background-color: #f9f9f9;
      color: #333;
    }
    h1, h2 {
      color: #2c3e50;
    }
    code {
      background: #eee;
      padding: 2px 4px;
      border-radius: 4px;
      font-family: monospace;
    }
    ul {
      padding-left: 20px;
    }
    .section {
      margin-bottom: 30px;
    }
    .highlight {
      background: #dff0d8;
      padding: 10px;
      border-left: 5px solid #3c763d;
      margin: 10px 0;
    }
  </style>
</head>
<body>

  <h1>🥦 Grocery Ordering System</h1>

  <p><strong>Project Title:</strong> Grocery Store Checkout System (Python Beginner Team Challenge)</p>
  <p><strong>Objective:</strong> To simulate a real-life grocery store checkout experience using Python, focusing on inventory management, cart operations, delivery options, and budget handling — ideal for beginner to intermediate Python learners.</p>

  <div class="section">
    <h2>✅ Updated Features</h2>

    <h3>📦 Product Inventory Management</h3>
    <ul>
      <li>Each grocery item now has a defined stock quantity.</li>
      <li>Stock is decreased when an item is added to the cart.</li>
      <li>If out of stock, the system alerts the user.</li>
    </ul>

    <h3>🛡 Robust Input Handling</h3>
    <ul>
      <li>Invalid product entries are caught using <code>try-except</code>.</li>
      <li>Friendly error message: “⚠ We do not sell that here. Please choose a product from the menu.”</li>
      <li>Prevents crashes from unexpected input.</li>
    </ul>

    <h3>🛒 Dynamic Cart Operations</h3>
    <ul>
      <li>Users can view and remove items from their cart.</li>
      <li>Inventory adjusts when items are removed (stock increases).</li>
    </ul>

    <h3>💰 Budget Handling</h3>
    <ul>
      <li>Total cart value is compared to the user’s budget at checkout.</li>
      <li>Options for insufficient funds:
        <ul>
          <li>Add more money</li>
          <li>Remove items</li>
          <li>Cancel purchase</li>
        </ul>
      </li>
    </ul>

    <h3>🚚 Delivery Logic</h3>
    <ul>
      <li>Users choose whether to have their items delivered.</li>
      <li>Orders above R1000 get free delivery.</li>
      <li>Otherwise, R2 per 500g of food.</li>
      <li>Charges are proportional (e.g. 2kg = R8 delivery fee).</li>
    </ul>

    <h3>🧾 Clear Summary and Messages</h3>
    <ul>
      <li>Readable cart summary, total cost, and payment feedback.</li>
      <li>Successful payment: thank-you and change displayed.</li>
      <li>Failed payment: friendly exit message.</li>
    </ul>

    <h3>🔧 Modular and Maintainable</h3>
    <ul>
      <li>Logic split into reusable functions: <code>add_to_cart</code>, <code>remove_from_cart</code>, <code>handle_payment</code>, <code>show_cart</code>.</li>
      <li>Clean and scalable — ready for future integration.</li>
    </ul>

    <h3>🖥 Tkinter GUI Ready</h3>
    <p>The console version is structured for easy migration to a GUI:</p>
    <ul>
      <li>Listboxes for item selection</li>
      <li>Buttons for add/remove</li>
      <li>Entry fields for user payments</li>
      <li>Checkboxes/radio buttons for delivery options</li>
      <li>Dynamic label updates for cart and cost</li>
    </ul>
  </div>

  <div class="section highlight">
    <strong>📌 Summary:</strong> This project mimics a real shopping experience with stock tracking, cart management, delivery fees, and budgeting. It uses Python fundamentals like functions, conditionals, loops, lists, and dictionaries. The system is now modular and ready for a Tkinter GUI upgrade.
  </div>

  <div class="section">
    <h2>🚀 Next Steps for Team</h2>
    <ul>
      <li>Test logic in the console version</li>
      <li>Assign GUI elements to teammates</li>
      <li>Start designing GUI layout</li>
    </ul>
    <p><strong>Let’s build it!</strong></p>
  </div>

</body>
</html>
