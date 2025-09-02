# Snack Bar System in Python

This is a simple terminal-based project that simulates the operation of a snack bar. It uses fundamental data structures such as queue, stack, dictionary, and lists to manage orders, bills, and sales history.

⚠️ Note: The source code is written in Portuguese, including variable names, function names, and user interface messages.

## Project Structure
- `app.py` →  Main user interface (menu)
- `cardapio.py` → Defines the menu with items, prices, preparation times, and categories
- `cozinha.py` → Automatically processes the order queue using `threading`
- `caixa.py` → Manages table bills, invoice history, and bill closing
- `stack.py` → Stack structure implementation (`Stack`).

## Features

- View menu by category (Snacks, Drinks, Desserts)
- Create orders for a specific table
- Automatically process orders in a preparation queue
- Simulated preparation time, handled in the background
- Deliver order and automatically charge the table’s bill
- View a table’s bill with item names and total amount
- Close the bill (generates a receipt added to the stack history)
- View sales history (latest receipts on top – stack behavior)
- Undo the last sale (removes the last receipt from history and restores the bill)

## Data Structures Used

- **Dictionary**: to represent the menu and table bills
- **Queue**: for processing orders in order of arrival (kitchen)
- **Stack**: for storing receipts (most recent payment on top)
- **Lists**: for storing items within an order

## ▶ How to Run

1. Make sure Python is installed (version 3.7 or higher)
2. Save all files in the same folder
3. In the terminal, run:
`python app.py`

You're good to go!
