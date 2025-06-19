import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Global variables
current_player = "X"
buttons = []

# Function to check for a winner
def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]
    
    for combo in winning_combinations:
        a, b, c = combo
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] and buttons[a]["text"] != "":
            messagebox.showinfo("Game Over", f"Player {buttons[a]['text']} wins!")
            reset_board()
            return
    
    # Check for tie
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Game Over", "It's a Tie!")
        reset_board()

# Function to handle button click
def on_click(index):
    global current_player
    if buttons[index]["text"] == "":
        buttons[index]["text"] = current_player
        check_winner()
        current_player = "O" if current_player == "X" else "X"

# Function to reset the board
def reset_board():
    global current_player
    current_player = "X"
    for button in buttons:
        button["text"] = ""

# Create buttons for Tic-Tac-Toe grid
for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 20), height=2, width=5, command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Create restart button
restart_button = tk.Button(root, text="Restart", font=("Arial", 14), command=reset_board)
restart_button.grid(row=3, column=0, columnspan=3)

# Run the Tkinter event loop
root.mainloop()
