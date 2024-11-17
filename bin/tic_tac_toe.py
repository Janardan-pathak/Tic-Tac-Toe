import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.resizable(False, False)

# Game variables
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]

# Colors and styles
bg_color = "#FAF3DD"
line_color = "#546A7B"
x_color = "#FF6B6B"
o_color = "#4ECDC4"
grid_size = 100


# Function to draw the game board
def draw_board(canvas):
    for i in range(1, 3):  # Draw vertical lines
        canvas.create_line(
            i * grid_size, 0, i * grid_size, 3 * grid_size, width=4, fill=line_color
        )
    for i in range(1, 3):  # Draw horizontal lines
        canvas.create_line(
            0, i * grid_size, 3 * grid_size, i * grid_size, width=4, fill=line_color
        )


# Function to handle a click on the canvas
def click(event):
    global current_player

    # Determine which cell was clicked
    x, y = event.x // grid_size, event.y // grid_size

    # Check if the cell is empty
    if board[y][x] == "":
        # Update the board and draw the player's symbol
        board[y][x] = current_player
        draw_symbol(x, y)

        # Check for a winner or a draw
        if check_winner():
            canvas.unbind("<Button-1>")  # Disable further clicks
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_board()
        elif check_draw():
            canvas.unbind("<Button-1>")  # Disable further clicks
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
        else:
            # Switch to the other player
            current_player = "O" if current_player == "X" else "X"


# Function to draw a player's symbol
def draw_symbol(x, y):
    x_center, y_center = x * grid_size + grid_size // 2, y * grid_size + grid_size // 2
    if current_player == "X":
        canvas.create_line(
            x * grid_size + 20,
            y * grid_size + 20,
            x * grid_size + 80,
            y * grid_size + 80,
            width=4,
            fill=x_color,
        )
        canvas.create_line(
            x * grid_size + 80,
            y * grid_size + 20,
            x * grid_size + 20,
            y * grid_size + 80,
            width=4,
            fill=x_color,
        )
    else:
        canvas.create_oval(
            x * grid_size + 20,
            y * grid_size + 20,
            x * grid_size + 80,
            y * grid_size + 80,
            width=4,
            outline=o_color,
        )


# Function to check for a winner
def check_winner():
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":  # Row
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":  # Column
            return True
    if board[0][0] == board[1][1] == board[2][2] != "":  # Diagonal
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":  # Anti-diagonal
        return True
    return False


# Function to check for a draw
def check_draw():
    return all(cell != "" for row in board for cell in row)


# Function to reset the board
def reset_board():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    canvas.delete("all")
    draw_board(canvas)
    canvas.bind("<Button-1>", click)


# Create a canvas for the game board
canvas = tk.Canvas(
    root, width=3 * grid_size, height=3 * grid_size, bg=bg_color, highlightthickness=0
)
canvas.pack()

# Draw the initial game board
draw_board(canvas)

# Bind the click event
canvas.bind("<Button-1>", click)

# Start the main loop
root.mainloop()
